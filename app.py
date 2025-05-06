import streamlit as st
from presentation_parser import extract_pptx_text
from feedback_engine import analyze_slide
from design_checks import run_design_checks
import os

st.set_page_config(page_title="📊 Pitch Deck Labs: AI Presentation Reviewer", layout="wide")
st.title("📊 Pitch Deck Labs: AI Presentation Reviewer")

purpose = st.text_input("What’s the purpose of this presentation? (e.g. Fundraising, Internal Update, Sales Pitch, etc.)")

uploaded_file = st.file_uploader("Upload your presentation file (PPTX, PDF, DOCX)", type=["pptx", "pdf", "docx"])

if uploaded_file:
    slides = extract_pptx_text(uploaded_file)
    for slide in slides:
        st.markdown(f"### Slide {slide['slide_number']}")
        st.markdown(f"**Title:** {slide['title']}")
        st.markdown(f"**Body:** {slide['body']}")
        feedback = analyze_slide(slide, purpose)
        st.markdown("💡 **AI Feedback**")
        st.markdown(feedback)
