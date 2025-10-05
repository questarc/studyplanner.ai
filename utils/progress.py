import matplotlib.pyplot as plt
import streamlit as st

def render_progress_chart(completed, total):
    if total == 0:
        st.warning("No tasks to track yet.")
        return
    fig, ax = plt.subplots()
    ax.pie([completed, total - completed], labels=["Completed", "Remaining"], autopct="%1.1f%%", colors=["#4CAF50", "#FFC107"])
    st.pyplot(fig)
