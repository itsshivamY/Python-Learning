import asyncio
import edge_tts
import pygame

async def main():
    text = input("Enter something here: ")

    voice = "en-US-JennyNeural"

    communicate = edge_tts.Communicate(text, voice)
    await communicate.save("human_voice.mp3")

asyncio.run(main())

pygame.mixer.init()
pygame.mixer.music.load("human_voice.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass