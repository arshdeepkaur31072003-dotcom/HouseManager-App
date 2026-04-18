import streamlit as st
import pandas as pd

st.set_page_config(page_title="Home Manager Pro", layout="wide")
st.title("🏠 Household Hub (Cloud Version)")

# --- SIMPLE GOOGLE SHEETS SETTINGS ---
# We will use a public CSV link from Google Sheets to keep it simple!
SHEET_ID = "YOUR_SHEET_ID_HERE"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"

st.write("Welcome! Once we link your Google Sheet, your data will appear here.")
st.info("Currently waiting for data connection...")