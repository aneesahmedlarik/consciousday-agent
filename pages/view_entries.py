# pages/view_entries.py
import streamlit as st
from db.database import fetch_entry_by_date
from datetime import date

st.title("📖 View Journal Entry")

selected_date = st.date_input("Select date to view")
if st.button("Load Entry"):
    entry = fetch_entry_by_date(str(selected_date))
    if entry:
        st.markdown("### 🪞 Reflection Output")
        st.markdown(entry)
    else:
        st.warning("No entry found for this date.")
