def subject_icon(subject):
    icons = {
        "Math": "📐",
        "Science": "🔬",
        "English": "📖",
        "History": "🏛️",
        "Computer": "💻"
    }
    return icons.get(subject, "📚")
