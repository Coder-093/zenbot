import random
from flask import Flask, request, jsonify, render_template
import simpleaudio as sa  # A library to play sound files

# Flask app setup
app = Flask(__name__)

# Motivational quotes to send to the user
motivational_quotes = [
    "You can do it! Stay focused!",
    "One step at a time. Keep going!",
    "Believe in yourself and keep pushing forward!"
]

# Simple ideas for short breaks
break_ideas = [
    "Stand up and stretch your arms.",
    "Take a quick walk around the room.",
    "Close your eyes and take five deep breaths."
]

# Function to play sound (e.g., rain or forest)
def play_sound(sound_file):
    # Plays the sound file given as input
    try:
        wave_obj = sa.WaveObject.from_wave_file(sound_file)  # Load the sound file
        play_obj = wave_obj.play()  # Play the sound
        play_obj.wait_done()  # Wait until the sound finishes
        return f"Playing sound from {sound_file}"  # Message confirming the sound is playing
    except Exception as e:
        # If there's an error, show it
        return f"Error playing sound: {e}"

# The main route for handling chat messages
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "").lower()  # Get the user's message

    # If the user wants to play a sound
    if "play" in user_message:
        if "rain" in user_message:
            return jsonify(response=play_sound("sounds/rain.wav"))
        elif "forest" in user_message:
            return jsonify(response=play_sound("sounds/forest.wav"))
        else:
            return jsonify(response="Please choose either 'Rain' or 'Forest'.")

    # If the user wants to take a break
    elif "take a break" in user_message:
        suggestion = random.choice(break_ideas)  # Pick a random suggestion
        return jsonify(response=suggestion)

    # If the user wants motivation
    elif "motivate" in user_message:
        quote = random.choice(motivational_quotes)  # Pick a random quote
        return jsonify(response=quote)

    # If the input doesn't match any known commands
    else:
        return jsonify(response="Sorry, I didn't understand that. Try 'play a sound', 'take a break', or 'motivate me'.")

# Route for the main chatbot interface
@app.route('/')
def home():
    return render_template('index.html')  # This will show the UI

# Start the app when the file runs
if __name__ == '__main__':
    app.run(debug=True)  # Debug mode for easier testing



