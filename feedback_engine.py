import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

def analyze_slide(slide, desc=""):
    prompt = f"""You are a presentation expert and creative strategist at Pitch Deck Labs.
Presentation Goal: {desc}
Slide content:
Title: {slide['title']}
Body: {slide['body']}
Give 2 short bullet-point strengths and 2 improvement suggestions. Keep it concise and useful.
"""
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
