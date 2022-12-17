import speech_recognition as sr

# Set up the speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

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
#This code will listen for a command from the user and try to recognize it using the Google Speech Recognition service. If the command is recognized, it will be printed to the console.

#Once you have the user's command, you can use it to control your home automation system. For example, you might use an if statement to check for specific commands, like "turn on the lights" or "set the temperature to 72 degrees." You can then use the phue library (or any other library you are using to control your home automation system) to execute the appropriate actions.

#Here is an example of how you might use an if statement to control your lights based on a voice command:

#Copy code
if "turn on the lights" in command:
    for light in lights:
        light.on = True
elif "turn off the lights" in command:
    for light in lights:
        light.on = False
#This code will turn the lights on if the user says "turn on the lights," and turn the lights off if the user says "turn off the lights." You can add additional if statements or use other control structures like while loops to add more functionality to your voice-activated home automation system.
if "turn on the lights" in command:
    for light in lights:
        light.on = True
elif "turn off the lights" in command:
    for light in lights:
        light.on = False


