import streamlit as st
from datetime import date
from planner_agent import study_planner_agent
from utils.icons import subject_icon

st.set_page_config(page_title="Study Planner Agent", page_icon="🧠", layout="wide")
st.title("🧠 Study Planner Agent")
st.markdown("Plan your week, track progress, and stay motivated!")

# Input Section
st.sidebar.header("📋 Enter Your Subjects & Exam Dates")
subjects = []
exams = {}

subject_input = st.sidebar.text_input("Add a subject (e.g., Math)")
exam_date = st.sidebar.date_input("Exam Date", value=date.today())

if st.sidebar.button("➕ Add Subject"):
    if subject_input:
        subjects.append(subject_input)
        exams[subject_input] = (exam_date - date.today()).days

# Run LangGraph Agent
if st.sidebar.button("📅 Generate Plan"):
    result = study_planner_agent.invoke({"subjects": subjects, "exams": exams})
    plan = result["plan"]
    quote = result["quote"]

    st.subheader("📆 Weekly Study Plan")
    for subject, tasks in plan.items():
        st.markdown(f"### {subject_icon(subject)} {subject}")
        for task in tasks:
            st.checkbox(task)

    st.markdown("---")
    st.subheader("💡 Motivation")
    st.info(f"**{quote}**")
