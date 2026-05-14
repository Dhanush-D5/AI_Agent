import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():

    with sr.Microphone() as source:

        print("\nListening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(
            source,
            timeout=5,
            phrase_time_limit=10
        )

    try:
        text = recognizer.recognize_google(audio)

        print(f"\nYou: {text}\n")

        return text.lower()

    except sr.UnknownValueError:
        return ""

    except Exception as e:
        print(e)
        return ""