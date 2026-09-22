import asyncio
import edge_tts
import pygame

async def main():
    text = """सुप्रभात सौरव भाई! 

आपको आपकी शादी के लिए एडवांस में बहुत-बहुत बधाई! 🎉💍

आप सोच रहे होंगे कि मैं एआई हूँ... 😂

लेकिन नहीं! मैं हूँ एक प्यारी सी लड़की! 

मुझे खास तौर पर कहा गया है और हां शिवम के तरफ से भी कि मैं आपको व्यक्तिगत रूप से शादी की शुभकामनाएँ दूँ। 💐

आपकी शादीशुदा ज़िंदगी हमेशा खुशियों से भरी रहे।

आप दोनों हमेशा खुश रहें और आपकी जोड़ी हमेशा बनी रहे। 

एक बार फिर से, सौरव भाई, आपको बहुत-बहुत बधाई! 

धन्यवाद दोस्तों! 

और हाँ...

मित्रों... 😎

धन्यवाद! """

    voice = "hi-IN-SwaraNeural"

    communicate = edge_tts.Communicate(
        text,
        voice,
        rate="-12%",
        pitch="+8Hz",
        volume="+0%"
    )

    await communicate.save("sourav.mp3")


asyncio.run(main())

pygame.mixer.init()
pygame.mixer.music.load("sourav.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pass

pygame.mixer.quit()