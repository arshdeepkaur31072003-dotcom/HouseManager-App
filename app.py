import streamlit as st
import pandas as pd
import requests
from datetime import datetime

# --- CONFIG ---
st.set_page_config(page_title="House Manager Pro", layout="wide")

# REPLACE THIS with the URL you copied in Step 1
SCRIPT_URL = "https://script.google.com/macros/s/AKfycbx_FS7A6lEGKosq57eqy8sHw_6mlz1itHC6ZYyQXQatRAZP8WQskZKgvNESYDIGWtqZSw/exec"
SHEET_ID = "105N_R5ZGz-IQTv6YDt70ZtAHmWCBpisdtuYs8qkOlW8"
READ_URL = f"https://docs.google.com/spreadsheets/d/1O5N_R5ZGz-IQTV6YDt70ZtAHmWCbpisdtuYs8qkOlW8/edit?usp=sharing"

st.title("🏠 House Manager Pro (Live Sync)")

# --- SHARED DATA LOADING ---
def load_data():
    return pd.read_csv(READ_URL)

df = load_data()

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Dashboard & Balances", "➕ Add Expense/Task", "📜 History"])

with tab1:
    if not df.empty:
        arsh = df[df['Paid By'] == 'Arshdeep']['Amount'].sum()
        nish = df[df['Paid By'] == 'Nishant']['Amount'].sum()
        diff = (arsh - nish) / 2
        
        c1, c2 = st.columns(2)
        c1.metric("Arshdeep Paid", f"₹{arsh}")
        c2.metric("Nishant Paid", f"₹{nish}")
        
        if diff > 0: st.success(f"Nishant owes Arshdeep ₹{abs(diff)}")
        elif diff < 0: st.warning(f"Arshdeep owes Nishant ₹{abs(diff)}")
        
        st.write("### Pending Tasks")
        st.dataframe(df[df['Status'] == 'Pending'])

with tab2:
    st.subheader("Add New Entry")
    with st.form("entry_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        date = col1.date_input("Date", datetime.now()).strftime("%Y-%m-%d")
        cat = col2.selectbox("Category", ["Expense", "Task", "Nomination"])
        item = st.text_input("Description / Item Name")
        amt = st.number_input("Amount (0 if Task)", min_value=0)
        p_by = st.selectbox("Member", ["Arshdeep", "Nishant"])
        stat = st.selectbox("Status", ["Completed", "Pending"])
        
        if st.form_submit_button("Save to Cloud"):
            payload = {
                "date": date, "category": cat, "item": item, 
                "amount": amt, "paid_by": p_by, "status": stat
            }
            # Sending data to the Secret Bridge
            response = requests.post(SCRIPT_URL, json=payload)
            if response.status_code == 200:
                st.balloons()
                st.success("Saved Successfully! Refreshing...")
                st.rerun()

with tab3:
    st.subheader("Full History Log")
    st.dataframe(df.sort_values(by="Date", ascending=False), use_container_width=True)