from voice.listen import listen
from voice.speak import speak

from brain.ai import (
    ask_ai,
    extract_memory
)

from commands.tools import (
    open_app,
    open_website
)

from commands.automation import (
    type_text,
    press_key,
    take_screenshot
)

from memory.memory import (
    load_memory,
    add_memory
)


def main():

    # Load persistent memory
    memory = load_memory()

    speak("Hello. I am Jarvis.")

    while True:

        user_input = listen()

        if not user_input:
            continue

        # Exit
        if "exit" in user_input:
            speak("Goodbye")
            break

        # =========================
        # MEMORY EXTRACTION
        # =========================

        important_memory = extract_memory(
            user_input
        )

        if important_memory != "NONE":

            add_memory(
                memory,
                important_memory
            )

            print("\nMEMORY SAVED:")
            print(important_memory)

        # =========================
        # AI RESPONSE
        # =========================

        result = ask_ai(
            user_input,
            memory
        )

        tool_needed = result.get(
            "tool_needed"
        )

        # =========================
        # TOOL EXECUTION
        # =========================

        if tool_needed:

            action = result.get("action")

            # OPEN APP
            if action == "open_app":

                response = open_app(
                    result.get("target")
                )

            # OPEN WEBSITE
            elif action == "open_website":

                response = open_website(
                    result.get("target")
                )

            # TYPE TEXT
            elif action == "type_text":

                response = type_text(
                    result.get("target")
                )

            # PRESS KEY
            elif action == "press_key":

                response = press_key(
                    result.get("target")
                )

            # SCREENSHOT
            elif action == "take_screenshot":

                response = take_screenshot()

            else:

                response = (
                    "I don't know how "
                    "to do that yet."
                )

        # =========================
        # NORMAL CONVERSATION
        # =========================

        else:

            response = result.get(
                "response"
            )

        # Speak response
        speak(response)


if __name__ == "__main__":
    main()