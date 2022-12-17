import gtts
import pygame

# Read the sensor data
moisture = read_moisture_sensor()
temperature = read_temperature_sensor()
humidity = read_humidity_sensor()
pH = read_pH_sensor()

# Generate the appropriate text string based on the sensor data
if moisture < 50:
    text = "Warning: soil moisture is low."
elif temperature > 30:
    text = "Warning: temperature is high."
elif humidity < 70:
    text = "Warning: humidity is low."
elif pH < 7:
    text = "Warning: pH is low."
else:
    text = "All sensor readings are within normal range."

# Generate the audio file
tts = gtts.gTTS(text)
tts.save("report.mp3")

# Play the audio file
pygame.mixer.init()
pygame.mixer.music.load("report.mp3")
pygame.mixer.music.play()
