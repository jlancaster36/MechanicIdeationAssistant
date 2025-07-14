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
    if 'design_notes' not in st.session_state:
        st.session_state.design_notes = {}
    if 'cognitive_reflection' not in st.session_state:
        st.session_state.cognitive_reflection = {}
    if 'idea_evolution' not in st.session_state:
        st.session_state.idea_evolution = []

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

# Cognitive design strategies to guide users through proven design thinking patterns
COGNITIVE_STRATEGIES = {
    "Pattern Recognition": {
        "description": "Identify familiar patterns from your inspiration sources",
        "questions": [
            "What core mechanics from your inspiration sources could be adapted?",
            "What patterns do you recognize across different media?",
            "How do these patterns relate to your narrative theme?"
        ]
    },
    "Analogical Reasoning": {
        "description": "Draw parallels between different domains",
        "questions": [
            "What real-world processes mirror your narrative conflict?",
            "How do your inspiration sources handle similar themes?",
            "What unexpected connections can you make?"
        ]
    },
    "Constraint Analysis": {
        "description": "Identify and work within design constraints",
        "questions": [
            "What limitations might enhance creativity?",
            "What technical constraints should inform your design?",
            "How can restrictions become features?"
        ]
    },
    "Mental Simulation": {
        "description": "Mentally test your ideas before implementation",
        "questions": [
            "How would players discover this mechanic?",
            "What edge cases might break this system?",
            "How does this mechanic evolve over time?"
        ]
    }
}

def generate_mechanic_suggestions(prompt: str, sources: List[str], schema: str, 
                                fun: int, novelty: int, visual: int) -> List[Dict[str, Any]]:
    """Generate mechanic suggestions using cognitive design principles"""
    
    suggestions = []
    
    # Enhanced schema suggestions with cognitive rationale
    schema_suggestions = {
        "Emotion States": [
            {
                "mechanic": "Emotional Resonance System where character abilities change based on emotional state",
                "cognitive_rationale": "Uses embodied cognition - physical abilities reflect mental states",
                "design_pattern": "State-dependent mechanics"
            },
            {
                "mechanic": "Empathy Mechanic where understanding NPC emotions unlocks new dialogue options",
                "cognitive_rationale": "Leverages theory of mind - understanding others' mental states",
                "design_pattern": "Social cognition mechanics"
            },
            {
                "mechanic": "Mood-Based World Interaction where environment responds to character's emotional state",
                "cognitive_rationale": "Reflects emotional contagion - emotions spread to environment",
                "design_pattern": "Emotional feedback loops"
            }
        ],
        "Karma System": [
            {
                "mechanic": "Ripple Effect System where small actions create large consequences over time",
                "cognitive_rationale": "Models causal reasoning and long-term thinking",
                "design_pattern": "Delayed consequence mechanics"
            },
            {
                "mechanic": "Moral Compass Mechanic where ethical choices visually alter the game world",
                "cognitive_rationale": "Provides visual feedback for abstract moral concepts",
                "design_pattern": "Moral visualization systems"
            },
            {
                "mechanic": "Community Standing System where reputation affects available resources",
                "cognitive_rationale": "Reflects social cognition and reputation management",
                "design_pattern": "Social capital mechanics"
            }
        ],
        "Resource Tradeoff": [
            {
                "mechanic": "Life Force Exchange where health can be traded for magical abilities",
                "cognitive_rationale": "Creates decision-making frameworks around opportunity cost",
                "design_pattern": "Risk-reward mechanics"
            },
            {
                "mechanic": "Time vs. Power System where rushing costs resources but provides advantages",
                "cognitive_rationale": "Models temporal reasoning and strategic planning",
                "design_pattern": "Temporal constraint mechanics"
            },
            {
                "mechanic": "Social Capital Mechanic where relationships are a finite resource to be managed",
                "cognitive_rationale": "Represents social cognition as resource management",
                "design_pattern": "Social resource mechanics"
            }
        ],
        "Transformation": [
            {
                "mechanic": "Adaptive Evolution System where character abilities change based on playstyle",
                "cognitive_rationale": "Reflects learning and adaptation through emergent behavior",
                "design_pattern": "Emergent progression mechanics"
            },
            {
                "mechanic": "Environmental Shaping where player actions permanently alter the world",
                "cognitive_rationale": "Models lasting impact and environmental memory",
                "design_pattern": "Persistent world mechanics"
            },
            {
                "mechanic": "Identity Shift Mechanic where character's nature changes through story choices",
                "cognitive_rationale": "Represents personal growth and identity formation",
                "design_pattern": "Character evolution mechanics"
            }
        ],
        "Cooperation": [
            {
                "mechanic": "Symbiotic Partnership where two characters share abilities and weaknesses",
                "cognitive_rationale": "Models interdependence and shared mental models",
                "design_pattern": "Collaborative dependency mechanics"
            },
            {
                "mechanic": "Collective Memory System where group experiences enhance individual capabilities",
                "cognitive_rationale": "Represents distributed cognition and social learning",
                "design_pattern": "Social learning mechanics"
            },
            {
                "mechanic": "Harmony Mechanic where synchronizing actions with allies creates powerful effects",
                "cognitive_rationale": "Models coordination and shared intentionality",
                "design_pattern": "Synchronization mechanics"
            }
        ]
    }
    
    # Add default suggestions for other schemas
    default_schemas = ["Environmental Interaction", "Memory System", "Social Dynamics", "Puzzle Integration", "Narrative Choice"]
    for schema_name in default_schemas:
        if schema_name not in schema_suggestions:
            schema_suggestions[schema_name] = [
                {
                    "mechanic": f"{schema_name} mechanic that responds to player behavior",
                    "cognitive_rationale": "Engages pattern recognition and adaptive thinking",
                    "design_pattern": "Responsive system mechanics"
                }
            ]
    
    # Get base suggestions for the schema
    schema_key = schema.split(" - ")[0]
    base_suggestions = schema_suggestions.get(schema_key, schema_suggestions["Environmental Interaction"])
    
    # Apply cognitive design principles
    for i, suggestion_data in enumerate(base_suggestions[:3]):
        # Start with base mechanic
        modified_mechanic = suggestion_data["mechanic"]
        
        # Apply narrative integration (analogical reasoning)
        if "artifact" in prompt.lower():
            modified_mechanic += " triggered by interaction with mysterious objects"
        elif "unite" in prompt.lower():
            modified_mechanic += " that requires collaboration between opposing forces"
        elif "powers" in prompt.lower():
            modified_mechanic += " that adapts to character's changing abilities"
        elif "discover" in prompt.lower():
            modified_mechanic += " that reveals itself through exploration"
        
        # Apply inspiration source patterns (pattern recognition)
        inspiration_modifiers = []
        for source in sources:
            if "Zelda" in source:
                inspiration_modifiers.append("exploration-based discovery")
            elif "Dark Souls" in source:
                inspiration_modifiers.append("high-stakes, meaningful choices")
            elif "Portal" in source:
                inspiration_modifiers.append("environmental puzzle integration")
            elif "Ghibli" in source or "Spirited Away" in source:
                inspiration_modifiers.append("wonder and transformation themes")
            elif "Journey" in source:
                inspiration_modifiers.append("wordless emotional communication")
            elif "Undertale" in source:
                inspiration_modifiers.append("subversive expectation mechanics")
            elif "Bioshock" in source:
                inspiration_modifiers.append("environmental narrative integration")
        
        if inspiration_modifiers:
            modified_mechanic += f" featuring {', '.join(inspiration_modifiers[:2])}"
        
        # Apply constraint-based refinement (based on ratings)
        complexity_level = "Simple" if fun < 4 else "Moderate" if fun < 8 else "Complex"
        innovation_level = "Traditional" if novelty < 4 else "Creative" if novelty < 8 else "Revolutionary"
        visual_level = "Minimal" if visual < 4 else "Engaging" if visual < 8 else "Spectacular"
        
        # Add cognitive design justification
        suggestions.append({
            "title": f"Suggestion {i+1}",
            "description": modified_mechanic,
            "cognitive_rationale": suggestion_data["cognitive_rationale"],
            "design_pattern": suggestion_data["design_pattern"],
            "complexity": complexity_level,
            "innovation": innovation_level,
            "presentation": visual_level,
            "fun_score": fun,
            "novelty_score": novelty,
            "visual_score": visual,
            "mental_model": generate_mental_model_description(suggestion_data, sources)
        })
    
    return suggestions

def export_idea_summary(idea_data: Dict[str, Any]) -> str:
    """Export a formatted summary of the locked idea including cognitive insights"""
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

**Cognitive Analysis:**
- **Cognitive Rationale:** {suggestion.get('cognitive_rationale', 'N/A')}
- **Design Pattern:** {suggestion.get('design_pattern', 'N/A')}
- **Mental Model:** {suggestion.get('mental_model', 'N/A')}

**Design Attributes:**
- **Complexity:** {suggestion['complexity']}
- **Innovation Level:** {suggestion['innovation']}
- **Visual Presentation:** {suggestion['presentation']}

"""
    
    # Add cognitive reflection data if available
    if idea_data.get('cognitive_reflection'):
        summary += "\n## Design Thinking Process\n\n"
        for step_key, reflection_data in idea_data['cognitive_reflection'].items():
            summary += f"**{reflection_data['context'].title()}:** {reflection_data['reflection']}\n\n"
    
    # Add idea evolution if available
    if idea_data.get('idea_evolution'):
        summary += "\n## Idea Evolution Timeline\n\n"
        for evolution in idea_data['idea_evolution']:
            timestamp = datetime.fromisoformat(evolution['timestamp']).strftime("%H:%M:%S")
            summary += f"**{timestamp} - Step {evolution['step']} ({evolution['context']}):** {evolution['thought']}\n\n"
    
    return summary

def display_cognitive_guidance(step: int) -> None:
    """Display cognitive strategy guidance"""
    
    # Display cognitive strategy based on step
    strategy_mapping = {
        2: "Pattern Recognition",
        3: "Analogical Reasoning", 
        4: "Constraint Analysis",
        5: "Mental Simulation"
    }
    
    if step in strategy_mapping:
        strategy = strategy_mapping[step]
        st.sidebar.markdown(f"### 🧠 Cognitive Strategy: {strategy}")
        
        with st.sidebar.expander("Thinking Tips"):
            st.markdown(COGNITIVE_STRATEGIES[strategy]["description"])
            
            # Show standard questions
            for q in COGNITIVE_STRATEGIES[strategy]["questions"]:
                st.markdown(f"• {q}")
def capture_design_thinking(step: int, context: str) -> None:
    """Capture user's design thinking process"""
    with st.sidebar.expander(f"💭 Step {step} Reflection"):
        reflection_key = f"step_{step}_reflection"
        
        reflection = st.text_area(
            f"What are you thinking about {context}?",
            key=reflection_key,
            height=80,
            placeholder="Capture your thoughts, concerns, or insights..."
        )
        
        if reflection:
            st.session_state.cognitive_reflection[f"step_{step}"] = {
                "context": context,
                "reflection": reflection,
                "timestamp": datetime.now().isoformat()
            }
            
            # Add to idea evolution
            st.session_state.idea_evolution.append({
                "step": step,
                "context": context,
                "thought": reflection,
                "timestamp": datetime.now().isoformat()
            })

def display_working_memory_support() -> None:
    """Display current session context to support working memory"""
    st.sidebar.markdown("### 📝 Your Design Context")
    
    if st.session_state.narrative_prompt:
        st.sidebar.markdown(f"**Theme:** {st.session_state.narrative_prompt[:50]}...")
    
    if st.session_state.inspiration_sources:
        st.sidebar.markdown(f"**Inspiration:** {', '.join(st.session_state.inspiration_sources[:2])}")
    
    if st.session_state.mechanic_schema:
        schema_name = st.session_state.mechanic_schema.split(" - ")[0]
        st.sidebar.markdown(f"**Schema:** {schema_name}")
    
    if st.session_state.fun_rating:
        st.sidebar.markdown(f"**Ratings:** F:{st.session_state.fun_rating} N:{st.session_state.novelty_rating} V:{st.session_state.visual_appeal_rating}")

def analyze_narrative_elements(prompt: str) -> List[Dict[str, str]]:
    """Analyze narrative elements to identify mechanic opportunities"""
    elements = []
    
    if "artifact" in prompt.lower():
        elements.append({
            "type": "Object-Centered Conflict",
            "description": "Mechanics could involve object interaction, transformation, or power"
        })
    
    if "unite" in prompt.lower() or "together" in prompt.lower():
        elements.append({
            "type": "Cooperation Theme",
            "description": "Mechanics should emphasize collaboration and shared goals"
        })
    
    if "choice" in prompt.lower() or "choose" in prompt.lower():
        elements.append({
            "type": "Decision Point",
            "description": "Mechanics could involve meaningful player choices with consequences"
        })
    
    if "power" in prompt.lower():
        elements.append({
            "type": "Power Dynamics",
            "description": "Mechanics could explore gaining, losing, or transforming abilities"
        })
    
    if "discover" in prompt.lower():
        elements.append({
            "type": "Discovery Theme",
            "description": "Mechanics should reward exploration and revelation"
        })
    
    return elements if elements else [{"type": "Open Narrative", "description": "Flexible story allows for diverse mechanic approaches"}]

def identify_design_patterns(source: str) -> List[str]:
    """Identify key design patterns from inspiration sources"""
    patterns = {
        "The Legend of Zelda series": ["Environmental puzzles", "Tool-based progression", "Exploration rewards"],
        "Dark Souls series": ["Risk-reward mechanics", "Learning through failure", "Atmospheric storytelling"],
        "Portal series": ["Physics-based puzzles", "Narrative integration", "Incremental complexity"],
        "Studio Ghibli films": ["Wonder and discovery", "Environmental storytelling", "Emotional resonance"],
        "Journey": ["Wordless communication", "Collaborative exploration", "Emotional progression"],
        "Bioshock series": ["Environmental narrative", "Moral choice consequences", "Power progression"],
        "Final Fantasy series": ["Character growth systems", "Strategic combat", "Epic storytelling"],
        "Undertale": ["Subversive mechanics", "Moral complexity", "Meta-narrative"],
        "Hollow Knight": ["Atmospheric exploration", "Skill-based progression", "Environmental storytelling"],
        "Avatar: The Last Airbender": ["Elemental systems", "Character development", "Moral growth"]
    }
    
    return patterns.get(source, ["Unique design elements", "Innovative mechanics", "Memorable experiences"])

def generate_mental_model_description(suggestion_data: Dict, sources: List[str]) -> str:
    """Generate description of the mental model this mechanic creates"""
    pattern = suggestion_data.get("design_pattern", "")
    
    if "State-dependent" in pattern:
        return "Players develop mental models linking emotional states to gameplay capabilities"
    elif "Social cognition" in pattern:
        return "Players build understanding of NPC mental states and social dynamics"
    elif "Delayed consequence" in pattern:
        return "Players learn to think systemically about action-consequence relationships"
    elif "Moral visualization" in pattern:
        return "Players develop visual-spatial representations of abstract moral concepts"
    elif "Emotional feedback" in pattern:
        return "Players understand how their actions affect the emotional landscape"
    else:
        return "Players construct mental models of cause-and-effect relationships"


def main():
    """Main app function with cognitive design support"""
    init_session_state()
    
    # Header
    st.title("🎮 Mechanic Ideation Assistant (MIA)")
    st.markdown("*Brainstorm video game mechanics using cognitive design principles*")
    
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
    
    # Add cognitive guidance and working memory support
    display_cognitive_guidance(current_step)
    display_working_memory_support()
    
    # Main content based on current step
    if current_step == 1:
        st.header("Step 1: Select Narrative Prompt")
        st.markdown("*Choose a story theme that will guide your mechanic design*")
        
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
            
            # Add narrative analysis
            st.markdown("### 🎭 Narrative Analysis")
            st.markdown("Consider how your chosen narrative creates opportunities for mechanics:")
            
            narrative_elements = analyze_narrative_elements(st.session_state.narrative_prompt)
            for element in narrative_elements:
                st.markdown(f"• **{element['type']}**: {element['description']}")
            
            capture_design_thinking(1, "narrative selection")
            
            if st.button("Next: Choose Inspiration Sources"):
                st.session_state.current_step = 2
                st.rerun()
    
    elif current_step == 2:
        st.header("Step 2: Choose Inspiration Sources")
        st.markdown("*Select media that exemplifies good design patterns*")
        
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
            
            # Add pattern recognition support
            st.markdown("### 🔍 Pattern Recognition")
            st.markdown("Identify key patterns from your inspiration sources:")
            
            for source in inspiration_sources:
                patterns = identify_design_patterns(source)
                st.markdown(f"**{source}**: {', '.join(patterns)}")
            
            capture_design_thinking(2, "inspiration and pattern recognition")
            
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
        st.markdown("*Choose a framework to focus your design thinking*")
        
        mechanic_schema = st.selectbox(
            "Choose a mechanic schema to focus your design:",
            MECHANIC_SCHEMAS,
            index=0 if not st.session_state.mechanic_schema else MECHANIC_SCHEMAS.index(st.session_state.mechanic_schema)
        )
        
        st.session_state.mechanic_schema = mechanic_schema
        
        st.info(f"Selected schema: {mechanic_schema}")
        
        # Add analogical reasoning support
        st.markdown("### 🔗 Analogical Connections")
        st.markdown("Consider how this schema connects to your narrative and inspiration sources:")
        
        schema_name = mechanic_schema.split(" - ")[0]
        if st.session_state.inspiration_sources:
            st.markdown(f"**{schema_name}** patterns in your inspiration sources:")
            for source in st.session_state.inspiration_sources:
                patterns = identify_design_patterns(source)
                relevant_patterns = [p for p in patterns if any(word in p.lower() for word in schema_name.lower().split())]
                if relevant_patterns:
                    st.markdown(f"• **{source}**: {', '.join(relevant_patterns)}")
        
        capture_design_thinking(3, "schema selection and analogical reasoning")
        
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
        st.markdown("*Apply constraint analysis to refine your concept*")
        
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
        
        # Show current ratings with constraint analysis
        st.markdown("### 🎯 Constraint Analysis")
        st.markdown(f"**Fun:** {fun_rating}/10 | **Novelty:** {novelty_rating}/10 | **Visual Appeal:** {visual_rating}/10")
        
        # Provide constraint-based guidance
        if fun_rating < 5:
            st.warning("💡 Consider: How can you increase player engagement? What would make this more enjoyable?")
        if novelty_rating < 5:
            st.warning("💡 Consider: What unique twist could you add? How can you subvert expectations?")
        if visual_rating < 5:
            st.warning("💡 Consider: How can you make this more visually compelling? What would players see?")
        
        capture_design_thinking(4, "rating and constraint analysis")
        
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
        st.markdown("*Apply mental simulation to evaluate your ideas*")
        
        # Generate suggestions if not already generated
        if not st.session_state.generated_suggestions:
            with st.spinner("Generating mechanic suggestions using cognitive design principles..."):
                suggestions = generate_mechanic_suggestions(
                    st.session_state.narrative_prompt,
                    st.session_state.inspiration_sources,
                    st.session_state.mechanic_schema,
                    st.session_state.fun_rating,
                    st.session_state.novelty_rating,
                    st.session_state.visual_appeal_rating
                )
                st.session_state.generated_suggestions = suggestions
        
        # Display suggestions with cognitive information
        st.markdown("Based on your inputs and cognitive design principles:")
        
        for i, suggestion in enumerate(st.session_state.generated_suggestions):
            with st.expander(f"💡 {suggestion['title']}", expanded=True):
                st.markdown(f"**Description:** {suggestion['description']}")
                
                # Add cognitive rationale
                st.markdown(f"**🧠 Cognitive Rationale:** {suggestion.get('cognitive_rationale', 'N/A')}")
                st.markdown(f"**🎯 Design Pattern:** {suggestion.get('design_pattern', 'N/A')}")
                st.markdown(f"**🧩 Mental Model:** {suggestion.get('mental_model', 'N/A')}")
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**Complexity:** {suggestion['complexity']}")
                with col2:
                    st.markdown(f"**Innovation:** {suggestion['innovation']}")
                with col3:
                    st.markdown(f"**Presentation:** {suggestion['presentation']}")
        
        # Mental simulation prompts
        st.markdown("### 🎮 Mental Simulation")
        st.markdown("Mentally test these mechanics:")
        st.markdown("• How would a player first encounter this mechanic?")
        st.markdown("• What would mastery of this mechanic look like?")
        st.markdown("• How does this mechanic evolve throughout the game?")
        st.markdown("• What edge cases or exploits might emerge?")
        
        capture_design_thinking(5, "suggestion evaluation and mental simulation")
        
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
                    'suggestions': st.session_state.generated_suggestions,
                    'cognitive_reflection': st.session_state.cognitive_reflection,
                    'idea_evolution': st.session_state.idea_evolution
                }
                st.session_state.current_step = 6
                st.rerun()
    
    elif current_step == 6:
        st.header("Step 6: Export Your Idea")
        st.markdown("*Capture your complete design thinking process*")
        
        if st.session_state.locked_idea:
            st.success("🎉 Your idea has been locked in!")
            
            # Display summary with cognitive insights
            summary = export_idea_summary(st.session_state.locked_idea)
            
            st.markdown("### 📋 Complete Idea Summary:")
            st.markdown(summary)
            
            # Show cognitive process overview
            if st.session_state.cognitive_reflection:
                st.markdown("### 🧠 Your Design Thinking Journey")
                st.markdown("Here's how your thinking evolved through the process:")
                
                for step_key, reflection_data in st.session_state.cognitive_reflection.items():
                    step_num = step_key.split('_')[1]
                    with st.expander(f"Step {step_num}: {reflection_data['context'].title()}"):
                        st.markdown(reflection_data['reflection'])
                        st.markdown(f"*Captured at: {reflection_data['timestamp']}*")
            
            # Download button
            st.download_button(
                label="📥 Download Complete Summary",
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
    
    # Footer with cognitive design information
    st.sidebar.markdown("---")
    st.sidebar.markdown("**MIA v2.0**")
    st.sidebar.markdown("Mechanic Ideation Assistant")
    st.sidebar.markdown("*Powered by Cognitive Design Principles*")

if __name__ == "__main__":
    main()
