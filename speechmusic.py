import speech_recognition as sr
import pylast

# Set up the speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

# Set up the Last.fm API client
API_KEY = "your_api_key"
API_SECRET = "your_api_secret"
username = "your_lastfm_username"
password_hash = pylast.md5("your_lastfm_password")
network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)

# Start listening for commands
with mic as source:
    print("Listening for commands...")
    audio = r.listen(source)

# Try to recognize the command
try:
    command = r.recognize_google(audio)
    print(f"You said: {command}")
except sr.UnknownValueError:
    print("I couldn't understand what you said.")
except sr.RequestError as e:
    print(f"Error while accessing the Google Speech Recognition service: {e}")

# Use the command to control Raspotify
if "play" in command:
    network.playback.play()
elif "pause" in command:
    network.playback.pause()
elif "skip" in command:
    network.playback.skip()