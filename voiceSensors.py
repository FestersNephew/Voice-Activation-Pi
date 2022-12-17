import speech_recognition as sr
import sensor_library as sl

# Set up the speech recognition
r = sr.Recognizer()
mic = sr.Microphone()

while True:
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

    # Check for the "report" command
    if "report" in command:
        # Read the sensor data
        moisture = sl.read_moisture_sensor()
        temperature = sl.read_temperature_sensor()
        humidity = sl.read_humidity_sensor()
        pH = sl.read_pH_sensor()

        # Generate the report
        report = (f"Moisture: {moisture}%\n"
                  f"Temperature: {temperature}°C\n"
                  f"Humidity: {humidity}%\n"
                  f"pH: {pH}")

        print(report)
