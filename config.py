"""
Config file for PO CoPilot demo.
Stores SAP connection details (for future real SAP integration)
and environment settings.
"""

# SAP connection settings (fill only for real SAP integration)
SAP_API_URL = "https://sap.example.com/sap/opu/odata/sap/API_PURCHASEORDER_PROCESS_SRV"
SAP_API_USER = "your_user"
SAP_API_PASSWORD = "your_password"

# Demo mode flag
DEMO_MODE = True  # True = use mock data, False = connect to real SAP
