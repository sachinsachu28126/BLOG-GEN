import google.generativeai as genai
from dotenv import load_dotenv
import os
from prompts import build_prompt

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_blog(topic, tone):
    """
    Generate blog content.
    """

    prompt = build_prompt(
        topic,
        tone
    )

    response = model.generate_content(
        prompt
    )

    return response.text