# Enhanced Mechanic Ideation Assistant (MIA)

<div align="center">
  <h1>🎮 Enhanced MIA</h1>
  <p><strong>AI-Powered Video Game Mechanic Generation</strong></p>
  <p>Transform narrative ideas into sophisticated game mechanics using real game data and cognitive decision-making</p>
</div>

## 🌟 Features

### **Intelligent Decision Support**
- **Cognitive Load Theory Integration** - Reduces mental burden through structured guidance
- **Schema Theory Application** - Proven frameworks for design thinking
- **Mathematical Analysis** - Evidence-based recommendations with confidence scoring

### **Real Game Data Integration**
- **IGDB API Integration** - Access to thousands of real games
- **Dynamic Content** - Fresh game selections each session
- **Authentic Mechanics** - AI analysis of actual game mechanics

### **Sophisticated Analysis**
- **Deterministic Narrative Analysis** - Automatic theme, action, and subject extraction
- **Multi-source Synthesis** - Combines elements from multiple games
- **Schema-driven Enhancement** - Framework-specific mechanic improvements

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/jlancaster36/MechanicIdeationAssistant.git
cd MechanicIdeationAssistant
git checkout enhanced-mia
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables
Create a `.env` file in the root directory:
```bash
cp .env.example .env
```

Edit the `.env` file and add your API keys:
```
IGDB_CLIENT_ID=your_igdb_client_id_here
IGDB_CLIENT_SECRET=your_igdb_client_secret_here
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

### 4. Launch the Application
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 🔑 API Setup

### IGDB API (Required)
1. Go to [IGDB API](https://api.igdb.com/)
2. Create an account and register your application
3. Get your Client ID and Client Secret
4. Add them to your `.env` file

### Anthropic Claude API (Required)
1. Go to [Anthropic](https://www.anthropic.com/)
2. Create an account and get your API key
3. Add it to your `.env` file

## 📖 How to Use

### Step 1: Select Narrative Prompt
- Choose from preset story themes or create your own
- System automatically analyzes themes, actions, and subjects

### Step 2: Select Inspiration Games
- Browse or search real games from IGDB database
- Select 2-3 games with interesting mechanics

### Step 3: Extract Game Mechanics
- AI analyzes your selected games
- Extracts core mechanics in structured format

### Step 4: Select Mechanic Schema
- Choose from 10 design frameworks:
  - Emotion States, Karma System, Resource Tradeoff
  - Transformation, Cooperation, Environmental Interaction
  - Memory System, Social Dynamics, Puzzle Integration
  - Narrative Choice

### Step 5: Rate Your Concept
- Set Fun Factor, Novelty, and Visual Appeal ratings
- Get intelligent schema recommendations based on cognitive analysis

### Step 6: Generate Suggestions
- Receive 2-3 detailed mechanic suggestions
- Each combines narrative context, game mechanics, and schema framework

### Step 7: Export Results
- Download complete summary with source analysis
- Markdown format for easy sharing and documentation

## 🧠 Cognitive Framework

The Enhanced MIA uses advanced cognitive theories:

- **Cognitive Schema Theory** (Bartlett, 1932) - Mental models for design frameworks
- **Dual-Process Theory** (Kahneman) - Fast intuitive + slow deliberative reasoning
- **Cognitive Load Theory** (Sweller) - Structured support to reduce mental burden

### Decision Algorithm
```
IF mismatch_score > cognitive_threshold (2.5):
    RECOMMEND alternative schemas with evidence-based reasoning
ELSE:
    REINFORCE current schema choice
```

## 🏗️ Architecture

```
Enhanced MIA/
├── app.py                    # Main Streamlit application
├── igdb_client.py           # IGDB API integration
├── mechanic_extractor.py    # Claude API for mechanic analysis
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # This file
```

## 📊 Example Output

**Input:**
- Narrative: "A hero loses their powers and must find a new way to save the world"
- Games: The Legend of Zelda, Dark Souls
- Schema: Transformation
- Ratings: Fun=8, Novelty=9, Visual=7

**Output:**
> "**Adaptive Ability System** that evolves based on character development and story progression, activated through environmental exploration, linked to mysterious object interactions and ancient powers with progressive character evolution mechanics requiring collaborative decision-making between characters"

## 🧪 Testing

Run the comprehensive test suite:
```bash
python test_runner.py
```

This executes 15 test scenarios validating:
- Narrative analysis accuracy
- Schema recommendation effectiveness
- Decision-making intervention appropriateness
- Overall system performance

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **IGDB** for providing comprehensive game database
- **Anthropic** for Claude AI capabilities
- **Streamlit** for the web framework
- **Cognitive Science Research** for theoretical foundations

## 📞 Support

If you encounter issues:
1. Check the [Issues](https://github.com/jlancaster36/MechanicIdeationAssistant/issues) page
2. Ensure all API keys are correctly configured
3. Verify Python dependencies are installed
4. Check that you're using Python 3.8+

---

<div align="center">
  <p><strong>Enhanced MIA v1.0</strong></p>
  <p>Transforming narrative ideas into sophisticated game mechanics</p>
</div>
