# Bulls and Cows Game


A modern implementation of the classic "Bulls and Cows" number guessing game with both CLI and web interfaces powered by Streamlit.

## Game Rules

Bulls and Cows is a code-breaking game where:

- The computer generates a secret 4-digit number with unique digits
- You try to guess this number in as few attempts as possible
- After each guess, you get feedback in the form of:
  - **Bulls**: Correct digits in the correct position
  - **Cows**: Correct digits in the wrong position

For example, if the secret number is "7846" and you guess "7814", you get:
- 2 Bulls (7 and 4 are in the correct position)
- 1 Cow (8 is correct but in the wrong position)

## Features

- Two game interfaces: CLI for quick play and Streamlit web app for a richer experience
- Interactive feedback and guess history
- Game statistics tracking
- Clean, modern UI in the web version

## Requirements

- Python 3.7+
- For the web app: Streamlit

## Installation

Clone the repository:
```bash
git clone https://github.com/yourusername/bulls-and-cows.git
cd bulls-and-cows
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Web Application (Recommended)

Run the Streamlit app:
```bash
streamlit run src/web_app.py
```

Then open your browser at `http://localhost:8501` to play the game.

### Command Line Interface

For a quick game in the terminal:
```bash
python src/cli_game.py
```

## Running Tests

```bash
pytest tests/
```

## Project Structure

```
bulls-and-cows/
├── LICENSE
├── README.md
├── requirements.txt
├── .gitignore
├── src/
│   ├── __init__.py
│   ├── game_logic.py  # Core game logic
│   ├── cli_game.py    # Command-line interface
│   └── web_app.py     # Streamlit web application
└── tests/
    ├── __init__.py
    └── test_game_logic.py
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
