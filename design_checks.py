def run_design_checks(slide):
    issues = []

    if slide["text_count"] > 100:
        issues.append("Too much text – consider splitting the content.")
    if slide["text_count"] < 10:
        issues.append("Slide might be too empty or lacking content.")
    if not slide["title"]:
        issues.append("Missing or unclear slide title.")
    if not slide["has_image"]:
        issues.append("No visuals found – consider adding a chart or image.")
    if slide["bullet_count"] > 5:
        issues.append("Too many bullet points – break into multiple slides or use visuals.")

    if not issues:
        return "✅ Slide design looks good!"
    return "⚠️ Design Suggestions:\n- " + "\n- ".join(issues)