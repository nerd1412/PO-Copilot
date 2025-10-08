import json
from config import DEMO_MODE, SAP_API_URL, SAP_API_USER, SAP_API_PASSWORD

def load_json(path):
    """Load JSON file and return Python object"""
    with open(path, "r") as f:
        return json.load(f)

def get_sap_connection():
    """
    Returns SAP connection details.
    For demo, returns None.
    For real SAP integration, returns a dict with API details.
    """
    if DEMO_MODE:
        return None
    else:
        return {
            "url": SAP_API_URL,
            "user": SAP_API_USER,
            "password": SAP_API_PASSWORD
        }
