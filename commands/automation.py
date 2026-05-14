import pyautogui
import time

# Type text
def type_text(text):

    pyautogui.write(
        text,
        interval=0.05
    )

    return f"Typing {text}"

# Press keyboard key
def press_key(key):

    pyautogui.press(key)

    return f"Pressed {key}"

# Hotkeys
def hotkey(*keys):

    pyautogui.hotkey(*keys)

    return f"Pressed {' + '.join(keys)}"

# Take screenshot
def take_screenshot():

    screenshot = pyautogui.screenshot()

    screenshot.save("screenshot.png")

    return "Screenshot saved"