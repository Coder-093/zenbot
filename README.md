# ZenBot

ZenBot is a simple chatbot application built using Flask and Python. It offers a relaxing and motivational experience by playing sounds, providing break suggestions, and sharing motivational quotes.

---

## Features

- **Play Sounds**: Users can play relaxing sounds like rain or forest ambiance.
- **Motivational Quotes**: Get inspired with random motivational quotes.
- **Break Suggestions**: Suggestions for short breaks to help you relax.

---

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.7 or higher
- Virtual Environment (optional but recommended)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Coder-093/zenbot.git
   cd zenbot
   ```

2. Set up a virtual environment: (This is for Windows)

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Add sound files:

   - Ensure the following `.wav` files are present in the `sounds/` directory:
     - `rain.wav`
     - `forest.wav`

5. Run the application:

   ```bash
   python app.py
   ```

6. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```

---

## How to Use

1. Open the chatbot in your browser.
2. Type a command or click a suggestion button:
   - **Play Sounds**: `play rain` or `play forest`
   - **Take a Break**: `take a break`
   - **Motivate Me**: `motivate me`
3. The chatbot responds with actions or messages based on your input.

---

## Project Structure

```
zenbot/
├── app.py              # Main Flask application
├── sounds/             # Directory for sound files
│   ├── rain.wav
│   ├── forest.wav
├── templates/          # HTML templates
│   └── index.html
├── tests/              # Test scripts
│   └── test_play_sound.py
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## Tests

The `tests/` folder contains scripts for testing the project:

- `test_play_sound.py`: Verifies the functionality of sound playback using `simpleaudio`.

Run the test script:

```bash
python tests/test_play_sound.py
```

---

## Future Improvements

- Add more relaxing sounds.
- Integrate a database to save user preferences.
- Improve the frontend with modern frameworks like React or Vue.
- Deploy the chatbot to a live server using Heroku or Render.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/) - Micro web framework for Python.
- [simpleaudio](https://simpleaudio.readthedocs.io/) - Library for audio playback.
