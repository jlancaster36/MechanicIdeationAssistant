"""
Mechanic Ideation Assistant (MIA)
A Streamlit app for brainstorming video game mechanics based on narrative prompts and analogical reasoning.
"""

import streamlit as st
import json
from typing import List, Dict, Any
from datetime import datetime

# Configure the page
st.set_page_config(
    page_title="Mechanic Ideation Assistant (MIA)",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
def init_session_state():
    """Initialize all session state variables"""
    if 'current_step' not in st.session_state:
        st.session_state.current_step = 1
    if 'narrative_prompt' not in st.session_state:
        st.session_state.narrative_prompt = ""
    if 'inspiration_sources' not in st.session_state:
        st.session_state.inspiration_sources = []
    if 'mechanic_schema' not in st.session_state:
        st.session_state.mechanic_schema = ""
    if 'fun_rating' not in st.session_state:
        st.session_state.fun_rating = 5
    if 'novelty_rating' not in st.session_state:
        st.session_state.novelty_rating = 5
    if 'visual_appeal_rating' not in st.session_state:
        st.session_state.visual_appeal_rating = 5
    if 'generated_suggestions' not in st.session_state:
        st.session_state.generated_suggestions = []
    if 'locked_idea' not in st.session_state:
        st.session_state.locked_idea = None

# Data for the app
NARRATIVE_PROMPTS = [
    "A lonely traveler discovers an ancient artifact that changes their destiny",
    "Two warring factions must unite to face a greater threat",
    "A hero loses their powers and must find a new way to save the world",
    "A peaceful village is threatened by mysterious forces from another realm",
    "A group of unlikely allies must work together to solve an ancient puzzle",
    "A character must choose between personal desires and the greater good",
    "A world where magic is dying and technology is rising",
    "A character discovers they are not who they thought they were",
    "Custom prompt (enter your own)"
]

INSPIRATION_SOURCES = [
    "The Legend of Zelda series",
    "Dark Souls series",
    "Portal series",
    "Bioshock series",
    "Studio Ghibli films",
    "Avatar: The Last Airbender",
    "Final Fantasy series",
    "Metroid series",
    "Undertale",
    "Hollow Knight",
    "Journey",
    "The Witcher series",
    "Persona series",
    "Spirited Away",
    "Princess Mononoke",
    "Mass Effect series",
    "Bloodborne",
    "Celeste",
    "Outer Wilds",
    "Disco Elysium"
]

MECHANIC_SCHEMAS = [
    "Emotion States - Mechanics that reflect character emotions",
    "Karma System - Actions have moral consequences",
    "Resource Tradeoff - Players must balance competing resources",
    "Transformation - Characters or world changes over time",
    "Cooperation - Multiple characters must work together",
    "Environmental Interaction - World responds to player actions",
    "Memory System - Past actions influence present options",
    "Social Dynamics - Relationships affect gameplay",
    "Puzzle Integration - Problem-solving woven into core mechanics",
    "Narrative Choice - Player decisions shape the story"
]

def generate_mechanic_suggestions(prompt: str, sources: List[str], schema: str, 
                                fun: int, novelty: int, visual: int) -> List[Dict[str, Any]]:
    """Generate mechanic suggestions based on user inputs using rule-based logic"""
    
    suggestions = []
    
    # Base suggestions based on schema
    schema_suggestions = {
        "Emotion States": [
            "Emotional Resonance System where character abilities change based on emotional state",
            "Empathy Mechanic where understanding NPC emotions unlocks new dialogue options",
            "Mood-Based World Interaction where environment responds to character's emotional state"
        ],
        "Karma System": [
            "Ripple Effect System where small actions create large consequences over time",
            "Moral Compass Mechanic where ethical choices visually alter the game world",
            "Community Standing System where reputation affects available resources and allies"
        ],
        "Resource Tradeoff": [
            "Life Force Exchange where health can be traded for magical abilities",
            "Time vs. Power System where rushing costs resources but provides advantages",
            "Social Capital Mechanic where relationships are a finite resource to be managed"
        ],
        "Transformation": [
            "Adaptive Evolution System where character abilities change based on playstyle",
            "Environmental Shaping where player actions permanently alter the world",
            "Identity Shift Mechanic where character's nature changes through story choices"
        ],
        "Cooperation": [
            "Symbiotic Partnership where two characters share abilities and weaknesses",
            "Collective Memory System where group experiences enhance individual capabilities",
            "Harmony Mechanic where synchronizing actions with allies creates powerful effects"
        ],
        "Environmental Interaction": [
            "Living World System where environment has its own goals and reactions",
            "Elemental Bonding where player can form relationships with natural forces",
            "Echo Mechanic where past actions leave traces that affect future gameplay"
        ],
        "Memory System": [
            "Ancestral Knowledge where character inherits skills from previous generations",
            "Collective Unconscious where shared experiences unlock hidden abilities",
            "Temporal Echo System where past decisions influence present opportunities"
        ],
        "Social Dynamics": [
            "Trust Network where relationships between NPCs affect player options",
            "Cultural Exchange System where learning from others unlocks new abilities",
            "Influence Web where player actions ripple through social connections"
        ],
        "Puzzle Integration": [
            "Narrative Puzzle System where solving problems advances the story",
            "Mechanical Sympathy where understanding world mechanics solves challenges",
            "Collaborative Problem-Solving where multiple perspectives are needed"
        ],
        "Narrative Choice": [
            "Branching Destiny System where choices create parallel storylines",
            "Consequence Cascade where decisions have delayed, interconnected effects",
            "Perspective Shift Mechanic where seeing events from different viewpoints changes outcomes"
        ]
    }
    
    # Get base suggestions for the schema
    schema_key = schema.split(" - ")[0]
    base_suggestions = schema_suggestions.get(schema_key, ["Generic mechanic suggestion"])
    
    # Modify suggestions based on inspiration sources and ratings
    for i, suggestion in enumerate(base_suggestions[:3]):  # Take up to 3 suggestions
        modified_suggestion = suggestion
        
        # Add inspiration source influences
        if sources:
            if any("Zelda" in source for source in sources):
                modified_suggestion += " with exploration-based discovery elements"
            if any("Dark Souls" in source for source in sources):
                modified_suggestion += " featuring high-stakes, challenging interactions"
            if any("Portal" in source for source in sources):
                modified_suggestion += " with clever, physics-based puzzle elements"
            if any("Ghibli" in source or "Spirited Away" in source for source in sources):
                modified_suggestion += " emphasizing wonder and magical transformation"
        
        # Adjust based on ratings
        complexity = "Simple" if fun < 4 else "Moderate" if fun < 8 else "Complex"
        innovation = "Traditional" if novelty < 4 else "Creative" if novelty < 8 else "Revolutionary"
        presentation = "Minimal" if visual < 4 else "Engaging" if visual < 8 else "Spectacular"
        
        suggestions.append({
            "title": f"Suggestion {i+1}",
            "description": modified_suggestion,
            "complexity": complexity,
            "innovation": innovation,
            "presentation": presentation,
            "fun_score": fun,
            "novelty_score": novelty,
            "visual_score": visual
        })
    
    return suggestions

def export_idea_summary(idea_data: Dict[str, Any]) -> str:
    """Export a formatted summary of the locked idea"""
    summary = f"""
# Mechanic Ideation Summary
**Generated on:** {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

## Selected Inputs
**Narrative Prompt:** {idea_data['narrative_prompt']}

**Inspiration Sources:** {', '.join(idea_data['inspiration_sources'])}

**Mechanic Schema:** {idea_data['mechanic_schema']}

## Ratings
- **Fun Rating:** {idea_data['fun_rating']}/10
- **Novelty Rating:** {idea_data['novelty_rating']}/10
- **Visual Appeal Rating:** {idea_data['visual_appeal_rating']}/10

## Generated Mechanic Suggestions

"""
    
    for i, suggestion in enumerate(idea_data['suggestions'], 1):
        summary += f"""
### {suggestion['title']}
**Description:** {suggestion['description']}
- **Complexity:** {suggestion['complexity']}
- **Innovation Level:** {suggestion['innovation']}
- **Visual Presentation:** {suggestion['presentation']}

"""
    
    return summary

def main():
    """Main app function"""
    init_session_state()
    
    # Header
    st.title("🎮 Mechanic Ideation Assistant (MIA)")
    st.markdown("*Brainstorm video game mechanics through narrative prompts and analogical reasoning*")
    
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    
    if st.sidebar.button("Start Over"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    
    # Step indicator
    steps = ["Narrative", "Inspiration", "Schema", "Ratings", "Suggestions", "Export"]
    current_step = st.session_state.current_step
    
    st.sidebar.markdown("### Progress")
    for i, step in enumerate(steps, 1):
        if i == current_step:
            st.sidebar.markdown(f"**→ {i}. {step}**")
        elif i < current_step:
            st.sidebar.markdown(f"✓ {i}. {step}")
        else:
            st.sidebar.markdown(f"○ {i}. {step}")
    
    # Main content based on current step
    if current_step == 1:
        st.header("Step 1: Select Narrative Prompt")
        
        narrative_choice = st.selectbox(
            "Choose a narrative prompt to inspire your mechanic:",
            NARRATIVE_PROMPTS,
            index=0
        )
        
        if narrative_choice == "Custom prompt (enter your own)":
            custom_prompt = st.text_area(
                "Enter your custom narrative prompt:",
                height=100,
                placeholder="Describe your story concept..."
            )
            if custom_prompt:
                st.session_state.narrative_prompt = custom_prompt
        else:
            st.session_state.narrative_prompt = narrative_choice
        
        if st.session_state.narrative_prompt:
            st.success(f"Selected prompt: {st.session_state.narrative_prompt}")
            if st.button("Next: Choose Inspiration Sources"):
                st.session_state.current_step = 2
                st.rerun()
    
    elif current_step == 2:
        st.header("Step 2: Choose Inspiration Sources")
        
        inspiration_sources = st.multiselect(
            "Select 1-2 inspiration sources (games, movies, anime):",
            INSPIRATION_SOURCES,
            default=st.session_state.inspiration_sources,
            max_selections=2
        )
        
        custom_source = st.text_input(
            "Or add a custom inspiration source:",
            placeholder="Enter your own inspiration..."
        )
        
        if custom_source and custom_source not in inspiration_sources:
            inspiration_sources.append(custom_source)
        
        st.session_state.inspiration_sources = inspiration_sources
        
        if inspiration_sources:
            st.success(f"Selected sources: {', '.join(inspiration_sources)}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back"):
                    st.session_state.current_step = 1
                    st.rerun()
            with col2:
                if st.button("Next: Choose Mechanic Schema"):
                    st.session_state.current_step = 3
                    st.rerun()
    
    elif current_step == 3:
        st.header("Step 3: Select Mechanic Schema")
        
        mechanic_schema = st.selectbox(
            "Choose a mechanic schema to focus your design:",
            MECHANIC_SCHEMAS,
            index=0 if not st.session_state.mechanic_schema else MECHANIC_SCHEMAS.index(st.session_state.mechanic_schema)
        )
        
        st.session_state.mechanic_schema = mechanic_schema
        
        st.info(f"Selected schema: {mechanic_schema}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back"):
                st.session_state.current_step = 2
                st.rerun()
        with col2:
            if st.button("Next: Rate Your Idea"):
                st.session_state.current_step = 4
                st.rerun()
    
    elif current_step == 4:
        st.header("Step 4: Rate Your Idea")
        
        st.markdown("Rate your idea concept on the following dimensions:")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            fun_rating = st.slider(
                "Fun Factor",
                min_value=1, max_value=10, 
                value=st.session_state.fun_rating,
                help="How fun do you think this concept could be?"
            )
            st.session_state.fun_rating = fun_rating
        
        with col2:
            novelty_rating = st.slider(
                "Novelty",
                min_value=1, max_value=10,
                value=st.session_state.novelty_rating,
                help="How unique or innovative is this concept?"
            )
            st.session_state.novelty_rating = novelty_rating
        
        with col3:
            visual_rating = st.slider(
                "Visual Appeal",
                min_value=1, max_value=10,
                value=st.session_state.visual_appeal_rating,
                help="How visually interesting could this be?"
            )
            st.session_state.visual_appeal_rating = visual_rating
        
        # Show current ratings
        st.markdown("### Current Ratings:")
        st.markdown(f"**Fun:** {fun_rating}/10 | **Novelty:** {novelty_rating}/10 | **Visual Appeal:** {visual_rating}/10")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Back"):
                st.session_state.current_step = 3
                st.rerun()
        with col2:
            if st.button("Generate Suggestions"):
                st.session_state.current_step = 5
                st.rerun()
    
    elif current_step == 5:
        st.header("Step 5: Generated Mechanic Suggestions")
        
        # Generate suggestions if not already generated
        if not st.session_state.generated_suggestions:
            with st.spinner("Generating mechanic suggestions..."):
                suggestions = generate_mechanic_suggestions(
                    st.session_state.narrative_prompt,
                    st.session_state.inspiration_sources,
                    st.session_state.mechanic_schema,
                    st.session_state.fun_rating,
                    st.session_state.novelty_rating,
                    st.session_state.visual_appeal_rating
                )
                st.session_state.generated_suggestions = suggestions
        
        # Display suggestions
        st.markdown("Based on your inputs, here are some mechanic suggestions:")
        
        for i, suggestion in enumerate(st.session_state.generated_suggestions):
            with st.expander(f"💡 {suggestion['title']}", expanded=True):
                st.markdown(f"**Description:** {suggestion['description']}")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**Complexity:** {suggestion['complexity']}")
                with col2:
                    st.markdown(f"**Innovation:** {suggestion['innovation']}")
                with col3:
                    st.markdown(f"**Presentation:** {suggestion['presentation']}")
        
        # Action buttons
        col1, col2, col3 = st.columns(3)
        with col1:
            if st.button("← Back to Ratings"):
                st.session_state.current_step = 4
                st.rerun()
        with col2:
            if st.button("🔄 Generate New Ideas"):
                st.session_state.generated_suggestions = []
                st.rerun()
        with col3:
            if st.button("🔒 Lock In This Idea"):
                st.session_state.locked_idea = {
                    'narrative_prompt': st.session_state.narrative_prompt,
                    'inspiration_sources': st.session_state.inspiration_sources,
                    'mechanic_schema': st.session_state.mechanic_schema,
                    'fun_rating': st.session_state.fun_rating,
                    'novelty_rating': st.session_state.novelty_rating,
                    'visual_appeal_rating': st.session_state.visual_appeal_rating,
                    'suggestions': st.session_state.generated_suggestions
                }
                st.session_state.current_step = 6
                st.rerun()
    
    elif current_step == 6:
        st.header("Step 6: Export Your Idea")
        
        if st.session_state.locked_idea:
            st.success("🎉 Your idea has been locked in!")
            
            # Display summary
            summary = export_idea_summary(st.session_state.locked_idea)
            
            st.markdown("### Idea Summary:")
            st.markdown(summary)
            
            # Download button
            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name=f"mechanic_idea_summary_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                mime="text/markdown"
            )
            
            # Action buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("← Back to Suggestions"):
                    st.session_state.current_step = 5
                    st.rerun()
            with col2:
                if st.button("🆕 Start New Idea"):
                    for key in st.session_state.keys():
                        del st.session_state[key]
                    st.rerun()
        else:
            st.error("No idea locked in. Please go back and lock in your idea first.")
            if st.button("← Back to Suggestions"):
                st.session_state.current_step = 5
                st.rerun()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.markdown("**MIA v1.0**")
    st.sidebar.markdown("Mechanic Ideation Assistant")

if __name__ == "__main__":
    main()
