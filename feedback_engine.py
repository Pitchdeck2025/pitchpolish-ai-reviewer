import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_slide(slide):
    prompt = f"""
You are a presentation expert. Review this slide content:
Title: {slide['title']}
Body: {slide['body']}

Give 2 strengths and 2 improvement suggestions.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response['choices'][0]['message']['content']