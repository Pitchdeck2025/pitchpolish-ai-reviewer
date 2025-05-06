import streamlit as st
from presentation_parser import extract_pptx_text
from feedback_engine import analyze_slide
from design_checks import run_design_checks

st.set_page_config(page_title="📊 Pitch Deck Labs: AI Presentation Reviewer", layout="wide")

st.markdown(
    "<h1 style='font-family:Questrial, sans-serif; font-weight:700;'>📊 Pitch Deck Labs: <br>AI Presentation Reviewer</h1>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Upload your presentation file (PPTX, PDF, DOCX)", 
    type=["pptx", "pdf", "docx"]
)

google_slide_link = st.text_input("Or paste your Google Slides share link")
desc = st.text_input("What’s the purpose of this presentation? (e.g. Introduction, audience, fundraising, sales pitch, internal update etc)")

if uploaded_file:
    with st.spinner("Analyzing your presentation..."):
        slides = extract_pptx_text(uploaded_file)
        for slide in slides:
            st.markdown(f"### Slide {slide['slide_number']}")
            st.markdown(f"**Title:** {slide['title']}")
            st.markdown(f"**Body:** {slide['body']}")
            
            feedback = analyze_slide(slide, desc)
            design_tips = run_design_checks(slide)
            
            st.markdown(f"🧠 **AI Content Feedback:**\n{feedback}")
            st.markdown(f"🎨 **Design Feedback:**\n{design_tips}")

st.caption("⚠️ This AI-generated feedback is for initial review only. Please use professional judgment before applying changes.")