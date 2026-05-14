import os

def execute_command(command):

    if "open notepad" in command:
        os.system("notepad")
        return "Opening Notepad"

    elif "open youtube" in command:
        os.system("start https://youtube.com")
        return "Opening YouTube"

    return None