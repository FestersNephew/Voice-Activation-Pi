def generate_report():
    # Read the sensor data
    moisture = read_moisture_sensor()
    temperature = read_temperature_sensor()
    humidity = read_humidity_sensor()
    pH = read_pH_sensor()

    # Generate the report text
    report = (f"Moisture: {moisture}%\n"
              f"Temperature: {temperature}°C\n"
              f"Humidity: {humidity}%\n"
              f"pH: {pH}")

    return report

# Generate the audio file
text = generate_report()
tts = gtts.gTTS(text)
tts.save("report.mp3")

# Play the audio file
pygame.mixer.init()
pygame.mixer.music.load("report.mp3")
pygame.mixer.music.play()
