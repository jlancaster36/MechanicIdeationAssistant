"""
Mechanic Extractor for Enhanced MIA
Uses Anthropic Claude to extract unique gameplay mechanics from game data
"""

import anthropic
from typing import List, Dict, Any, Optional
import streamlit as st
import json
import re
from dataclasses import dataclass
from igdb_client import GameData

@dataclass
class GameMechanic:
    """Data class for extracted game mechanics"""
    game_name: str
    mechanic_summary: List[str]  # [noun, verb, subject]
    genres: List[str]
    themes: List[str]
    confidence: float

class MechanicExtractor:
    """Extracts unique gameplay mechanics from game data using Claude"""
    
    def __init__(self, api_key: str):
        self.client = anthropic.Anthropic(api_key=api_key)
        
    def extract_mechanic(self, game: GameData) -> Optional[GameMechanic]:
        """Extract unique gameplay mechanic from a single game"""
        prompt = self._create_prompt(game)
        
        try:
            response = self.client.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=100,
                temperature=0.3,
                system="You are a video game mechanics analyst. You must return exactly a three-element array in the specified format.",
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            
            content = response.content[0].text.strip()
            mechanic_array = self._parse_response(content)
            
            if mechanic_array and len(mechanic_array) == 3:
                return GameMechanic(
                    game_name=game.name,
                    mechanic_summary=mechanic_array,
                    genres=game.genres,
                    themes=game.themes,
                    confidence=1.0  # Could be enhanced with confidence scoring
                )
            else:
                st.warning(f"Invalid response format for {game.name}: {content}")
                return None
                
        except Exception as e:
            st.error(f"Error extracting mechanic for {game.name}: {str(e)}")
            return None
    
    def extract_mechanics_batch(self, games: List[GameData]) -> List[GameMechanic]:
        """Extract mechanics from multiple games"""
        mechanics = []
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, game in enumerate(games):
            status_text.text(f"Extracting mechanic from {game.name}...")
            
            mechanic = self.extract_mechanic(game)
            if mechanic:
                mechanics.append(mechanic)
            
            progress_bar.progress((i + 1) / len(games))
        
        progress_bar.empty()
        status_text.empty()
        
        return mechanics
    
    def _create_prompt(self, game: GameData) -> str:
        """Create the specific prompt for mechanic extraction"""
        return f"""Given the video game titled: "{game.name}",
and its genre classification: {game.genres},

Identify the **unique gameplay mechanic** that distinguishes this title from others in the same genre(s).
Output a three-word summary in the format [noun, verb, subject], where:

- **Noun** = Tool, object, or system used
- **Verb** = Action taken by the player
- **Subject** = Target or focus of the mechanic

Your output must be a **three-element array**, like: ["character", "swaps", "teammates"]

The summary should *highlight the differentiating mechanic*, not just the general gameplay loop."""
    
    def _parse_response(self, response: str) -> Optional[List[str]]:
        """Parse the GPT response to extract the three-element array"""
        # Try to find JSON array pattern
        json_pattern = r'\[.*?\]'
        matches = re.findall(json_pattern, response)
        
        for match in matches:
            try:
                parsed = json.loads(match)
                if isinstance(parsed, list) and len(parsed) == 3:
                    return [str(item).strip('"').strip("'").lower() for item in parsed]
            except json.JSONDecodeError:
                continue
        
        # Fallback: try to extract three quoted words
        word_pattern = r'["\'](.*?)["\']'
        words = re.findall(word_pattern, response)
        
        if len(words) >= 3:
            return [word.lower() for word in words[:3]]
        
        return None

@st.cache_data(ttl=3600)  # Cache for 1 hour
def get_cached_mechanics(api_key: str, games_data: List[GameData]) -> List[GameMechanic]:
    """Cached version of mechanic extraction"""
    # Convert GameData to dict for caching (dataclasses aren't hashable)
    games_dict = [
        {
            'id': game.id,
            'name': game.name,
            'genres': game.genres,
            'themes': game.themes,
            'summary': game.summary,
            'rating': game.rating,
            'rating_count': game.rating_count,
            'first_release_date': game.first_release_date
        }
        for game in games_data
    ]
    
    # Convert back to GameData objects
    games = [GameData(**game_dict) for game_dict in games_dict]
    
    extractor = MechanicExtractor(api_key)
    return extractor.extract_mechanics_batch(games)
