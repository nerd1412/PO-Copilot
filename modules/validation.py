def validate_po(po, po_history):
    issues = []

    # Check missing fields
    for field in ["PO_Number", "Vendor", "Material", "Quantity", "Price", "DeliveryDate"]:
        if not po.get(field):
            issues.append(f"Missing {field}")

    # Check for duplicate PO number
    if po["PO_Number"] in [p["PO_Number"] for p in po_history if p != po]:
        issues.append("Duplicate PO number found.")

    # Price anomaly (20% above historical average for same material)
    mat_pos = [p for p in po_history if p["Material"] == po["Material"] and p != po]
    if mat_pos:
        avg_price = sum(p["Price"] for p in mat_pos) / len(mat_pos)
        if po["Price"] > 1.2 * avg_price:
            issues.append(f"Price unusually high (Avg: {avg_price})")

    return issues
