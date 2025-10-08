def risk_analysis(po, vendor_master):
    risks = []

    # Vendor approval check
    if po["Vendor"] not in [v["Vendor"] for v in vendor_master]:
        risks.append("Vendor not in approved vendor list.")

    # Suspicious quantity
    if po["Quantity"] > 10000:
        risks.append("Quantity unusually high.")

    return risks
