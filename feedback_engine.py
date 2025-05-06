import openai
import streamlit as st

# Use API key from Streamlit secrets
openai.api_key = st.secrets["OPENAI_API_KEY"]

def analyze_slide(slide, desc=""):
    prompt = f"""
You are a presentation expert and creative strategist at Pitch Deck Labs.

Presentation Goal: {desc}

Slide content:
Title: {slide['title']}
Body: {slide['body']}

Give 2 short bullet-point strengths and 2 improvement suggestions. Keep it concise and useful.
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content
