import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Summarize this WordPress post title in one line: 'Top 5 Trading Strategies for Beginners'"
)
print(response.text)