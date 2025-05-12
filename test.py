import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
api_key = os.environ.get("GROQ_API_KEY")

# Check if key is actually loaded
if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file or environment variables.")

# Initialize client
client = Groq(api_key=api_key)

# Make request
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama-3.3-70b-versatile",
)

print(chat_completion.choices[0].message.content)
