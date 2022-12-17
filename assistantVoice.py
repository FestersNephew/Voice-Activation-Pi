import gtts
import pygame

# Generate the audio file
text = "Hello, this is your home assistant speaking. The current temperature is 30 degrees Celsius."
tts = gtts.gTTS(text)
tts.save("report.mp3")

# Play the audio file
pygame.mixer.init()
pygame.mixer.music.load("report.mp3")
pygame.mixer.music.play()
