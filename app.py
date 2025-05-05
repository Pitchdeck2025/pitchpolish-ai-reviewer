import streamlit as st
from presentation_parser import extract_pptx_text
from feedback_engine import analyze_slide
from design_checks import run_design_checks

st.title("📊 PitchPolish: AI Presentation Reviewer")
uploaded_file = st.file_uploader("Upload your .pptx file", type="pptx")

if uploaded_file:
    with st.spinner("Analyzing..."):
        slides = extract_pptx_text(uploaded_file)
        for slide in slides:
            st.markdown(f"### Slide {slide['slide_number']}")
            st.markdown(f"**Title:** {slide['title']}")
            st.markdown(f"**Body:** {slide['body']}")
            feedback = analyze_slide(slide)
            st.markdown(f"🧠 **AI Content Feedback:**\n{feedback}")
            design_tips = run_design_checks(slide)
            st.markdown(f"🎨 **Design Feedback:**\n{design_tips}")