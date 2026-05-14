from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Conversation memory
chat_history = []

def ask_ai(user_input):

    # Save user message
    chat_history.append(f"User: {user_input}")

    # Limit memory size
    if len(chat_history) > 10:
        chat_history.pop(0)

    conversation = "\n".join(chat_history)

    prompt = f"""
    You are Jarvis, a futuristic AI assistant.

    Speak naturally and conversationally.

    Conversation:
    {conversation}

    Jarvis:
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

    reply = response.choices[0].message.content

    # Save Jarvis reply
    chat_history.append(f"Jarvis: {reply}")

    return reply