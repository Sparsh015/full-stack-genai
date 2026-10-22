import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/"
)

response =client.chat.completions.create(
    model = "gemini-3.5-flash-lite",
    messages = [
        {"role": "user", "content": "YHey there! I am Sparsh. who are you specifically?"}
        ]
    )

print(response.choices[0].message.content)