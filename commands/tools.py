import os
import webbrowser

# Installed apps
apps = {
    "notepad": "notepad",
    "calculator": "calc",
}

# Websites
websites = {
    "youtube": "https://youtube.com",
    "google": "https://google.com",
    "github": "https://github.com",
}

def open_app(target):

    if target in apps:

        os.system(f"start {apps[target]}")

        return f"Opening {target}"

    return f"I could not find {target}"

import webbrowser

def open_website(target):

    # Remove spaces
    target = target.replace(" ", "")

    url = f"https://www.{target}.com"

    try:

        webbrowser.open(url)

        return f"Opening {target}"

    except:

        return f"Could not open {target}"