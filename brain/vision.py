import pytesseract
from PIL import Image
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\tesseract.exe"
)

# Groq client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_image(image_path):

    try:

        # Open screenshot
        image = Image.open(image_path)

        # OCR extraction
        extracted_text = pytesseract.image_to_string(
            image
        )

        # No readable text
        if extracted_text.strip() == "":

            return (
                "I could not detect readable text "
                "on the screen."
            )

        # Clean OCR text
        cleaned = extracted_text.replace(
            "\n",
            " "
        )

        cleaned = " ".join(
            cleaned.split()
        )

        # =========================
        # AI SCREEN UNDERSTANDING
        # =========================

        prompt = f"""
You are Jarvis Vision.

The following text was extracted
from the user's computer screen using OCR.

Your job:
- understand what is happening
- summarize the screen naturally
- explain important visible apps/pages
- keep response concise

SCREEN TEXT:
{cleaned}
"""

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        summary = (
            response
            .choices[0]
            .message
            .content
        )

        return summary

    except Exception as e:

        print("VISION ERROR:", e)

        return "I could not analyze the screen."