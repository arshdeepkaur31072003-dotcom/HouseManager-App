import streamlit as st
from streamlit_gsheets import GSheetConnection
import pandas as pd
import datetime

# --- APP CONFIG ---
st.set_page_config(page_title="Home Manager Pro", layout="wide")
st.title("🏠 Household Hub (Cloud Version)")

# --- GOOGLE SHEETS CONNECTION ---
# This looks for a secret "URL" that we will set up in Streamlit Cloud
conn = st.connection("gsheets", type=GSheetConnection)

# --- SIDEBAR & LOGIC ---
st.sidebar.header("🕹️ Control Panel")
st.info("This app is now connected to Google Sheets for permanent storage.")

# NOTE: For the Cloud version, we will use the Streamlit Dashboard 
# to manage the data directly in the Sheet for now to keep it simple!

# Fetch data from Google Sheets
tasks_df = conn.read(worksheet="Tasks")
users_df = conn.read(worksheet="Users")
exp_df = conn.read(worksheet="Expenses")

tab1, tab2, tab3 = st.tabs(["📅 Nomination Board", "📊 Expenses", "📜 History"])

with tab1:
    st.subheader("📅 Task Nomination Board")
    st.write("Current Tasks from Google Sheets:")
    st.dataframe(tasks_df)
    st.write("Tip: Update the Google Sheet directly to see changes here instantly!")

with tab2:
    st.subheader("🤝 Settle Up")
    st.write("Expense tracking live from your Google Drive.")
    st.dataframe(exp_df)