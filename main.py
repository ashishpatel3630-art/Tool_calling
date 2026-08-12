import os 
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Clients(
    api_key =os.getenv("GEMINI_API_KEY")
)
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b