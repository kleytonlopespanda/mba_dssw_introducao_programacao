import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('API_KEY')

client = genai.Client(api_key=API_KEY)

pergunta= input('Digite sua pergunta ao Gemini: ')

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=pergunta,
)

print (response.text)