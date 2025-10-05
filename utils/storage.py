import json

def export_plan(subjects, exams):
    with open("study_plan.json", "w") as f:
        json.dump({"subjects": subjects, "exams": exams}, f)

def load_plan():
    try:
        with open("study_plan.json", "r") as f:
            data = json.load(f)
            return data.get("subjects", []), data.get("exams", {})
    except FileNotFoundError:
        return [], {}
