from gtts import gTTS
import pygame

text = input("Enter something here: ")

sound = gTTS(text, lang="en")
sound.save("welcome2.mp3")

pygame.mixer.init()
pygame.mixer.music.load("welcome2.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass