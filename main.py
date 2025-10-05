import streamlit as st
from datetime import datetime, date
from planner_agent import study_planner_agent
from utils.icons import subject_icon

st.set_page_config(page_title="Study Planner Agent", page_icon="🧠", layout="wide")
st.title("🧠 Study Planner Agent")
st.markdown("Plan your week, track progress, and stay motivated!")

# Initialize session state
if "subjects" not in st.session_state:
    st.session_state.subjects = []

if "exams" not in st.session_state:
    st.session_state.exams = {}

# Sidebar input
st.sidebar.header("📋 Enter Your Subjects & Exam Dates")
subject_input = st.sidebar.text_input("Add a subject (e.g., Math)")
exam_date = st.sidebar.date_input("Exam Date", value=date.today())

if st.sidebar.button("➕ Add Subject"):
    if subject_input and subject_input not in st.session_state.subjects:
        st.session_state.subjects.append(subject_input)
        days_left = (exam_date - date.today()).days
        st.session_state.exams[subject_input] = max(days_left, 1)

# Generate plan
if st.sidebar.button("📅 Generate Plan"):
    result = study_planner_agent.invoke({
        "subjects": st.session_state.subjects,
        "exams": st.session_state.exams
    })

    plan = result.get("plan", {})
    quote = result.get("quote", "")

    if plan:
        st.subheader("📆 Weekly Study Plan")
        for subject, tasks in plan.items():
            st.markdown(f"### {subject_icon(subject)} {subject}")
            for task in tasks:
                st.checkbox(task)
    else:
        st.warning("No study plan generated. Please add subjects and exam dates.")

    st.markdown("---")
    st.subheader("💡 Motivation")
    st.info(f"**{quote}**")
