# Mechanic Ideation Assistant (MIA) 🎮

A Streamlit web application that helps game designers brainstorm video game mechanics through narrative prompts and analogical reasoning.

## Features

- **Step-by-step workflow** for mechanic ideation
- **Narrative prompt selection** from curated list or custom input
- **Inspiration source selection** from games, movies, and anime
- **Mechanic schema selection** for focused design
- **Rating system** for Fun, Novelty, and Visual Appeal
- **Rule-based suggestion generation** with 2-3 mechanic ideas
- **Idea locking and export** functionality
- **Clean, intuitive interface** with progress tracking

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

2. Open your browser and navigate to the provided URL (typically `http://localhost:8501`)

3. Follow the step-by-step process:
   - **Step 1**: Select a narrative prompt
   - **Step 2**: Choose 1-2 inspiration sources
   - **Step 3**: Pick a mechanic schema
   - **Step 4**: Rate your idea on three dimensions
   - **Step 5**: Review generated suggestions
   - **Step 6**: Lock in and export your idea

## Project Structure

```
MechanicIdeation/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # This file
├── .github/
│   └── copilot-instructions.md  # Copilot coding guidelines
└── .vscode/
    └── tasks.json     # VS Code tasks configuration
```

## How It Works

The app uses rule-based logic to generate mechanic suggestions based on:
- Selected narrative prompt
- Chosen inspiration sources
- Mechanic schema focus
- User ratings for fun, novelty, and visual appeal

Each suggestion includes:
- Detailed description
- Complexity assessment
- Innovation level
- Visual presentation notes

## Mechanic Schemas

The app includes 10 different mechanic schemas:
- Emotion States
- Karma System
- Resource Tradeoff
- Transformation
- Cooperation
- Environmental Interaction
- Memory System
- Social Dynamics
- Puzzle Integration
- Narrative Choice

## Inspiration Sources

Curated list includes popular games, movies, and anime known for innovative mechanics:
- Game series: Zelda, Dark Souls, Portal, Bioshock, Final Fantasy, etc.
- Studio Ghibli films
- Anime: Avatar: The Last Airbender
- Indie games: Undertale, Hollow Knight, Celeste, etc.

## Export Feature

Users can export their finalized ideas as markdown files containing:
- All selected inputs
- Ratings
- Generated suggestions
- Timestamp

## Development

This project uses:
- **Streamlit** for the web interface
- **Python 3.7+** for the backend logic
- **Session state management** for user data persistence
- **Rule-based generation** for mechanic suggestions

## Contributing

Feel free to fork this project and submit pull requests for improvements such as:
- Additional narrative prompts
- More inspiration sources
- New mechanic schemas
- Enhanced suggestion generation logic
- UI/UX improvements

## License

This project is open source and available under the MIT License.
