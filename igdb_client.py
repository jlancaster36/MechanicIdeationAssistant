"""
IGDB API Client for Enhanced MIA
Handles communication with the Internet Games Database API for fetching game data
"""

import requests
import time
import random
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import streamlit as st

@dataclass
class GameData:
    """Data class for game information"""
    id: int
    name: str
    genres: List[str]
    themes: List[str]
    summary: str
    rating: float
    rating_count: int
    first_release_date: int

class IGDBClient:
    """Client for interacting with the IGDB API"""
    
    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.token_expires_at = 0
        self.base_url = "https://api.igdb.com/v4"
        
    def _get_access_token(self) -> str:
        """Get OAuth access token from Twitch"""
        if self.access_token and time.time() < self.token_expires_at:
            return self.access_token
            
        auth_url = "https://id.twitch.tv/oauth2/token"
        auth_data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        
        response = requests.post(auth_url, data=auth_data)
        response.raise_for_status()
        
        token_data = response.json()
        self.access_token = token_data['access_token']
        self.token_expires_at = time.time() + token_data['expires_in'] - 300  # 5 min buffer
        
        return self.access_token
    
    def _make_request(self, endpoint: str, query: str) -> Dict[str, Any]:
        """Make authenticated request to IGDB API"""
        token = self._get_access_token()
        
        headers = {
            'Client-ID': self.client_id,
            'Authorization': f'Bearer {token}',
            'Accept': 'application/json'
        }
        
        response = requests.post(
            f"{self.base_url}/{endpoint}",
            headers=headers,
            data=query
        )
        response.raise_for_status()
        return response.json()
    
    def search_popular_games(self, limit: int = 20, offset: int = 0) -> List[GameData]:
        """Search for popular, well-known games"""
        # Query for games with good ratings and sufficient rating counts
        query = f"""
        fields name, genres.name, themes.name, summary, rating, rating_count, first_release_date;
        where rating >= 70 & rating_count >= 50 & themes != null;
        sort rating desc;
        limit {limit};
        offset {offset};
        """
        
        try:
            games_data = self._make_request("games", query)
            return self._parse_games_data(games_data)
        except Exception as e:
            st.error(f"Error fetching games: {str(e)}")
            return []
    
    def get_random_popular_games(self, count: int = 10) -> List[GameData]:
        """Get random selection of popular games"""
        # Get a larger pool and randomly select from it
        pool_size = min(count * 5, 100)  # Get 5x more than needed, max 100
        random_offset = random.randint(0, 500)  # Random starting point
        
        games_pool = self.search_popular_games(limit=pool_size, offset=random_offset)
        
        if len(games_pool) >= count:
            return random.sample(games_pool, count)
        else:
            return games_pool
    
    def search_games_by_name(self, name: str, limit: int = 10) -> List[GameData]:
        """Search for games by name"""
        query = f"""
        fields name, genres.name, themes.name, summary, rating, rating_count, first_release_date;
        where name ~ "{name}"* & rating_count >= 10;
        sort rating desc;
        limit {limit};
        """
        
        try:
            games_data = self._make_request("games", query)
            return self._parse_games_data(games_data)
        except Exception as e:
            st.error(f"Error searching games: {str(e)}")
            return []
    
    def _parse_games_data(self, games_data: List[Dict]) -> List[GameData]:
        """Parse raw API response into GameData objects"""
        parsed_games = []
        
        for game in games_data:
            try:
                # Extract genres
                genres = []
                if 'genres' in game:
                    genres = [genre['name'] for genre in game['genres']]
                
                # Extract themes
                themes = []
                if 'themes' in game:
                    themes = [theme['name'] for theme in game['themes']]
                
                # Skip games without genres or themes
                if not genres and not themes:
                    continue
                
                game_data = GameData(
                    id=game['id'],
                    name=game['name'],
                    genres=genres,
                    themes=themes,
                    summary=game.get('summary', ''),
                    rating=game.get('rating', 0),
                    rating_count=game.get('rating_count', 0),
                    first_release_date=game.get('first_release_date', 0)
                )
                parsed_games.append(game_data)
                
            except KeyError as e:
                st.warning(f"Skipping game due to missing data: {e}")
                continue
        
        return parsed_games

def get_cached_random_games(client_id: str, client_secret: str, count: int = 10) -> List[GameData]:
    """Get random games - no caching to ensure fresh results each time"""
    client = IGDBClient(client_id, client_secret)
    return client.get_random_popular_games(count)

@st.cache_data(ttl=1800)  # Cache for 30 minutes
def search_cached_games(client_id: str, client_secret: str, query: str, limit: int = 10) -> List[GameData]:
    """Cached version of game search - caching is appropriate for search since users expect consistent results"""
    client = IGDBClient(client_id, client_secret)
    return client.search_games_by_name(query, limit)
