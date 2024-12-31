import simpleaudio as sa
import wave

# Function to play a .wav file
def play_wave(file_path):
    try:
        # Open the file and load it for playback
        wave_obj = wave.open(file_path, 'rb')
        wave_audio = sa.WaveObject.from_wave_read(wave_obj)
        play_obj = wave_audio.play()
        play_obj.wait_done()  # Wait for the audio to finish
        print(f"Successfully played: {file_path}")
    except Exception as e:
        # Print an error if something goes wrong
        print(f"Could not play the file. Error: {e}")

# Testing the function
# Change the file path to test different sounds
print("Testing the sound playback function...")
play_wave("C:/Users/HP/Documents/Projects/zenbot/sounds/rain.wav")

