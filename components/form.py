# Streamlit form component
import streamlit as st

def journal_form():
    st.subheader("🌅 Morning Reflection Form")
    journal = st.text_area("Morning Journal")
    dream = st.text_area("Dream")
    intention = st.text_input("Intention of the Day")
    priorities = st.text_input("Top 3 Priorities (comma-separated)")
    return journal, dream, intention, priorities
