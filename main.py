import streamlit as st
from datetime import date
from planner_agent import study_planner_agent
from utils.icons import subject_icon
from utils.quotes import get_motivational_quote
from utils.gamify import award_xp, show_badges
from utils.progress import render_progress_chart
from utils.storage import export_plan, load_plan

st.set_page_config(page_title="Study Planner Agent", page_icon="🧠", layout="wide")
st.title("🧠 Study Planner Agent")
st.markdown("Plan your week, track progress, and stay motivated!")

# Initialize session state
if "subjects" not in st.session_state:
    st.session_state.subjects = []
if "exams" not in st.session_state:
    st.session_state.exams = {}
if "task_checks" not in st.session_state:
    st.session_state.task_checks = []
if "xp" not in st.session_state:
    st.session_state.xp = 0

# Sidebar input
st.sidebar.header("📋 Enter Your Subjects & Exam Dates")
subject_input = st.sidebar.text_input("Add a subject")
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
        total_tasks = 0
        completed_tasks = 0
        st.session_state.task_checks = []

        for subject, tasks in plan.items():
            st.markdown(f"### {subject_icon(subject)} {subject}")
            for i, task in enumerate(tasks):
                key = f"{subject}_{i}"
                checked = st.checkbox(task, key=key)
                st.session_state.task_checks.append(checked)
                total_tasks += 1
                if checked:
                    completed_tasks += 1
                    award_xp()

        render_progress_chart(completed_tasks, total_tasks)
        show_badges()

        st.markdown("---")
        st.subheader("💡 Motivation")
        st.info(f"**{quote}**")
    else:
        st.warning("No study plan generated. Please add subjects and exam dates.")

# Save/load buttons
st.sidebar.markdown("---")
if st.sidebar.button("💾 Save Plan"):
    export_plan(st.session_state.subjects, st.session_state.exams)

if st.sidebar.button("📂 Load Plan"):
    subjects, exams = load_plan()
    st.session_state.subjects = subjects
    st.session_state.exams = exams
    st.success("Plan loaded successfully!")
