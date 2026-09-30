import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    config={
        #"system_instruction": """Answer every question in one sentence."""
        "system_instruction": """Answer every question in detail using simple language and examples."""
        },
    #contents="tell me what happens when i place an api call to the gemini api with a question"
    contents="why are api keys needed in dev work?"
)

print(response.text)


