def run_design_checks(slide):
    tips = []
    if slide["text_count"] > 80:
        tips.append("🔻 Too much text on this slide. Try simplifying.")
    if not slide["has_image"]:
        tips.append("🖼️ Consider adding a visual to support the message.")
    if slide["bullet_count"] > 5:
        tips.append("• Too many bullet points. Consider splitting or simplifying.")
    return "\n".join(tips) if tips else "✅ Design looks clean!"
