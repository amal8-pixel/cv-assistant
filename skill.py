def review_resume(text: str) -> dict:
    """تحليل أساسي لنص السيرة الذاتية"""
    keywords = ["Python", "Dart", "Flutter", "JavaScript", "HTML", "CSS", "Git", "SQL"]
    found_skills = [kw for kw in keywords if kw.lower() in text.lower()]
    
    suggestions = []
    if "Git" not in found_skills:
        suggestions.append("إضافة أدوات إدارة النسخ مثل Git تُعزز من قوة السيرة الذاتية.")
    if len(found_skills) < 3:
        suggestions.append("يُفضل توسيع قسم المهارات التقنية وإضافة أدوات أو تقنيات إضافية.")
        
    return {
        "extracted_skills": found_skills,
        "suggestions": suggestions if suggestions else ["السيرة الذاتية متوازنة وتغطي مهارات أساسية جيدة."]
    }