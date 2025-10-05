import streamlit as st

def award_xp():
    st.session_state.xp += 10

def show_badges():
    xp = st.session_state.xp
    st.markdown(f"**XP Points:** {xp}")
    if xp >= 100:
        st.success("🏅 Level 1 Achieved!")
    if xp >= 200:
        st.success("🥇 Level 2 Unlocked!")
    if xp >= 300:
        st.success("🎖️ Level 3 Mastery!")
