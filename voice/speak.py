import edge_tts
import asyncio
from playsound import playsound
import os

async def generate_voice(text):

    communicate = edge_tts.Communicate(
        text,
        voice="en-US-GuyNeural"
    )

    await communicate.save("voice.mp3")

def speak(text):

    print(f"\nJarvis: {text}\n")

    asyncio.run(generate_voice(text))

    playsound("voice.mp3")

    os.remove("voice.mp3")