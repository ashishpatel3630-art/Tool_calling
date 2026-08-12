import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Clients(
    api_key =os.getenv("GEMINI_API_KEY")
)
