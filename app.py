import streamlit as st
import pandas as pd

# --- APP CONFIG ---
st.set_page_config(page_title="Home Manager Pro", layout="wide")
st.title("🏠 Household Hub (Cloud Version)")

# --- GOOGLE SHEETS CONNECTION ---
# Using your specific ID here
SHEET_ID = "105N_R5ZGz-IQTv6YDt70ZtAHmWCBpisdtuYs8qkOlW8"
url = f"https://docs.google.com/spreadsheets/d/1O5N_R5ZGz-IQTV6YDt70ZtAHmWCbpisdtuYs8qkOlW8/gviz/tq?tqx=out:csv"

try:
    # This part reads the data from your Google Sheet
    df = pd.read_csv(url)
    st.success("✅ Connected to Google Sheets!")
    st.write("### Current Household Data:")
    st.dataframe(df)
except Exception as e:
    st.error("Waiting for connection...")
    st.info("Make sure your Google Sheet is set to 'Anyone with the link can view'.")

st.sidebar.info("This app is live from GitHub and stays on 24/7!")