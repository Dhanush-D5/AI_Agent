from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_ai(user_input):

    prompt = prompt = f"""
You are Jarvis, an intelligent futuristic AI assistant.

RULES:

1. If the user wants you to perform an action
like:
- opening apps
- opening websites
- controlling the computer

THEN return JSON.

2. If the user is simply talking,
asking questions,
or having a conversation,

respond naturally like ChatGPT.

Examples:

User: Open YouTube
{{
    "tool_needed": true,
    "action": "open_website",
    "target": "youtube"
}}

User: Open calculator
{{
    "tool_needed": true,
    "action": "open_app",
    "target": "calculator"
}}

User: Explain machine learning
Machine learning is a field of AI where...

User: Tell me a joke
Why did the programmer quit his job?

User: {user_input}
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

    text = response.choices[0].message.content.strip()

    # Try parsing JSON
    try:

        cleaned = text.replace("```json", "").replace("```", "").strip()

        return json.loads(cleaned)

    except:

        # Normal chat fallback
        return {
            "tool_needed": False,
            "response": text
        }