from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Conversation memory
conversation_history = []


# =========================
# MAIN AI FUNCTION
# =========================

def ask_ai(user_input, memory):

    # Store user message
    conversation_history.append(
        f"User: {user_input}"
    )

    # Limit conversation size
    if len(conversation_history) > 10:
        conversation_history.pop(0)

    history = "\n".join(conversation_history)

    memory_text = "\n".join(memory)

    prompt = f"""
You are Jarvis, an intelligent futuristic AI assistant.

You can:
- have natural conversations
- answer questions intelligently
- control the computer using tools
- analyze screenshots and screens

You have access to long-term memory.

Use it naturally while responding.

Long-term memory:
{memory_text}

Conversation History:
{history}

RULES:

1. If the user wants you to PERFORM an action,
return ONLY raw JSON.

DO NOT:
- explain
- talk
- add markdown
- add sentences

Your entire response must be JSON only.

2. If the user is simply chatting,
explaining,
asking questions,
or having a conversation,
respond naturally like ChatGPT.

3. NEVER return explanations together with JSON.

AVAILABLE ACTIONS:

- open_website
- open_app
- type_text
- press_key
- take_screenshot
- analyze_screen

JSON FORMAT:

{{
    "tool_needed": true,
    "action": "action_name",
    "target": "value"
}}

EXAMPLES:

User: Open YouTube
{{
    "tool_needed": true,
    "action": "open_website",
    "target": "youtube"
}}

User: Open Flipkart
{{
    "tool_needed": true,
    "action": "open_website",
    "target": "flipkart"
}}

User: Open calculator
{{
    "tool_needed": true,
    "action": "open_app",
    "target": "calculator"
}}

User: Type hello world
{{
    "tool_needed": true,
    "action": "type_text",
    "target": "hello world"
}}

User: Press enter
{{
    "tool_needed": true,
    "action": "press_key",
    "target": "enter"
}}

User: Take screenshot
{{
    "tool_needed": true,
    "action": "take_screenshot"
}}

User: What's on my screen?
{{
    "tool_needed": true,
    "action": "analyze_screen"
}}

User: Analyze my screen
{{
    "tool_needed": true,
    "action": "analyze_screen"
}}

User: What can you see on the screen?
{{
    "tool_needed": true,
    "action": "analyze_screen"
}}

User: Explain machine learning
Machine learning is a field of AI...

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

    # Save assistant response
    conversation_history.append(
        f"Jarvis: {text}"
    )

    print("\nAI RAW RESPONSE:")
    print(text)

    # =========================
    # TRY PARSING JSON
    # =========================

    try:

        cleaned = text.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()

        # Find JSON anywhere
        start = cleaned.find("{")
        end = cleaned.rfind("}") + 1

        if start != -1 and end != -1:

            json_text = cleaned[start:end]

            parsed = json.loads(json_text)

            return parsed

    except Exception as e:

        print("JSON ERROR:", e)

    # =========================
    # NORMAL CHAT FALLBACK
    # =========================

    return {
        "tool_needed": False,
        "response": text
    }


# =========================
# MEMORY EXTRACTION
# =========================

def extract_memory(user_input):

    prompt = f"""
You are a memory extraction system.

Your job is to extract useful long-term memory
from the user's message.

Examples of useful memory:
- user's name
- preferences
- favorite things
- goals
- habits
- projects
- important personal details

IMPORTANT:
Return ONLY the memory sentence.

If nothing important exists,
return ONLY:
NONE

Message:
{user_input}
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

    memory = response.choices[0].message.content.strip()

    # Remove markdown formatting
    memory = memory.replace(
        "```",
        ""
    ).strip()

    return memory