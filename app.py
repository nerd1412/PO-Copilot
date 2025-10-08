import streamlit as st
from streamlit_option_menu import option_menu
from modules.utils import load_json, get_sap_connection
from modules.validation import validate_po
from modules.risk_check import risk_analysis
from modules.summarizer import generate_summary
from config import DEMO_MODE

# ----------------------
# Load data
# ----------------------
if DEMO_MODE:
    po_data = load_json("data/po_data.json")
    vendor_master = load_json("data/vendor_master.json")
else:
    sap_conn = get_sap_connection()
    po_data = []
    vendor_master = []

# ----------------------
# Streamlit page config
# ----------------------
st.set_page_config(page_title="PO CoPilot", layout="wide")
st.title("🚀 PO CoPilot – AI Assistant for Purchase Orders")
st.markdown("Professional, minimal design demonstrating PO challenges and AI solutions.")

# ----------------------
# PO Selection
# ----------------------
if po_data:
    po_numbers = [po["PO_Number"] for po in po_data]
    selected_po_number = st.selectbox("Select a Purchase Order:", po_numbers)
    po = next(p for p in po_data if p["PO_Number"] == selected_po_number)
else:
    st.warning("No PO data available. Set DEMO_MODE=True for demo or connect to SAP.")
    po = None

# ----------------------
# Sidebar Menu
# ----------------------
with st.sidebar:
    selected_tab = option_menu(
        menu_title="Navigation",
        options=["PO Details", "Validation & Risks", "AI Summary", "Features & Differentiators"],
        icons=["file-earmark-text", "exclamation-triangle", "robot", "info-circle"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "5px", "background-color": "#101d47"},  # Navy blue
            "icon": {"color": "#1abc9c", "font-size": "18px"},               # Teal icon
            "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px",
                         "--hover-color": "#444", "color":"#f0f0f0"},       # Light text
            "nav-link-selected": {"background-color": "#1abc9c", "color":"#333"}  # Active dark grey
        }
    )

# ----------------------
# Tab Content
# ----------------------
if po:
    if selected_tab == "PO Details":
        st.subheader("📑 Purchase Order Details")
        st.json(po)

    elif selected_tab == "Validation & Risks":
        issues = validate_po(po, po_data)
        risks = risk_analysis(po, vendor_master)

        st.subheader("⚠️ Issues Detected")
        if issues:
            for i, issue in enumerate(issues, 1):
                st.markdown(f"{i}. ❌ {issue}")
        else:
            st.success("✅ No issues found.")

        st.subheader("⚠️ Risks Detected")
        if risks:
            for i, risk in enumerate(risks, 1):
                st.markdown(f"{i}. ⚠️ {risk}")
        else:
            st.success("✅ No risks found.")

    elif selected_tab == "AI Summary":
        issues = validate_po(po, po_data)
        risks = risk_analysis(po, vendor_master)

        st.subheader("🧠 AI Summary for Procurement Team")
        # Use st.success for consistent light green background
        st.success(generate_summary(po, issues, risks))

    elif selected_tab == "Features & Differentiators":
        st.subheader("🌟 PO CoPilot Unique Features")
        st.markdown("""
        - **AI-powered PO validation**: Detects missing fields, duplicates, price anomalies, and quantity anomalies per PO.
        - **Risk analysis**: Flags unapproved vendors and suspicious quantities.
        - **AI summary**: Human-readable summary combining issues & risks for procurement teams.
        - **Future-proof SAP integration**: Works with mock data now; ready to fetch real SAP data via APIs.
        - **Customizable & modular**: Can be extended without changing SAP MM module.
        - **Vendor communication simulation (optional)**: Parse unstructured emails for PO updates.

        **Differences from SAP Joule & Ariba:**
        - Joule: Summarizes data but **does not detect anomalies per PO or generate AI summary combining risks**.
        - Ariba: Supplier risk exists at vendor level only; **no per-PO anomaly detection or plain-language AI summary**.
        - Our demo: **All-in-one AI assistant**, fully modular and free for demonstration purposes.
        """)
