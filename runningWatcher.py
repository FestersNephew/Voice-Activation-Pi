while True:
    # Read the sensor data and generate the audio output
    moisture = read_moisture_sensor()
    temperature = read_temperature_sensor()
    humidity = read_humidity_sensor()
    pH = read_pH_sensor()
    report = generate_report()
    tts = gtts.gTTS(report)
    tts.save("report.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("report.mp3")
    pygame.mixer.music.play()
