from voice.listen import listen
from voice.speak import speak
from brain.ai import ask_ai
from commands.system_commands import execute_command

def main():

    speak("Hello, I am Jarvis.")

    while True:

        command = listen()

        if command == "":
            continue

        if "exit" in command:
            speak("Goodbye")
            break

        # Try command execution
        result = execute_command(command)

        if result:
            speak(result)

        else:
            response = ask_ai(command)
            speak(response)

if __name__ == "__main__":
    main()