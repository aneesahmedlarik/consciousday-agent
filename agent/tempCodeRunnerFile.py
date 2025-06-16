# LangChain agent logic using PROMPT_TEMPLATE
import streamlit as st
from components.form import journal_form
from components.output import display_outputs
from agent.prompt_agent import generate_reflection
from db.database import init_db, insert_entry, fetch_entry_by_date
from datetime import date

st.set_page_config(page_title="ConsciousDay Agent")
st.title("🧘 ConsciousDay Agent")

init_db()

if 'response' not in st.session_state:
    st.session_state.response = None

with st.sidebar:
    st.markdown("### 📅 View Previous Reflections")
    selected_date = st.date_input("Pick a date")
    if st.button("Load Entry"):
        entry = fetch_entry_by_date(str(selected_date))
        if entry:
            st.session_state.response = entry
        else:
            st.warning("No entry found for this date.")

# Main form
journal, dream, intention, priorities = journal_form()

if st.button("Reflect and Plan"):
    with st.spinner("Thinking..."):
        result = generate_reflection(journal, dream, intention, priorities)
        if result:
            insert_entry(date.today(), journal, dream, intention, priorities, result)
            st.session_state.response = result
        else:
            st.error("Failed to generate reflection. Please try again.")

# Show results
if st.session_state.response:
    display_outputs(st.session_state.response)
