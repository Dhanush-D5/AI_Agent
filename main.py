from voice.listen import listen
from voice.speak import speak

from brain.ai import ask_ai

from commands.tools import (
    open_app,
    open_website
)

def main():

    speak("Hello. I am Jarvis.")

    while True:

        user_input = listen()

        if not user_input:
            continue

        if "exit" in user_input:
            speak("Goodbye")
            break

        result = ask_ai(user_input)

        action = result.get("action")

        # OPEN APP
        if action == "open_app":

            target = result.get("target")

            response = open_app(target)

            speak(response)

        # OPEN WEBSITE
        elif action == "open_website":

            target = result.get("target")

            response = open_website(target)

            speak(response)

        # NORMAL CHAT
        else:

            response = result.get("response")

            speak(response)

if __name__ == "__main__":
    main()