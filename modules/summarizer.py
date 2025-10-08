def generate_summary(po, issues=None, risks=None):
    """
    Summarize the following Purchase Order in clear, professional language suitable for the procurement team.
    """
    summary_lines = []

    # Basic PO details
    summary_lines.append(f"Purchase Order Number: {po.get('PO_Number')}")
    summary_lines.append(f"Vendor: {po.get('Vendor')}")
    summary_lines.append(f"Material: {po.get('Material')}")
    summary_lines.append(f"Quantity: {po.get('Quantity')}")
    summary_lines.append(f"Price: {po.get('Price')}")
    summary_lines.append(f"Delivery Date: {po.get('Delivery_Date')}")

    # Issues
    if issues:
        summary_lines.append("\nDetected Issues:")
        for i, issue in enumerate(issues, 1):
            summary_lines.append(f"{i}. {issue}")
    else:
        summary_lines.append("\nNo issues detected.")

    # Risks
    if risks:
        summary_lines.append("\nPotential Risks:")
        for i, risk in enumerate(risks, 1):
            summary_lines.append(f"{i}. {risk}")
    else:
        summary_lines.append("\nNo risks detected.")

    # Add professional note
    summary_lines.append("\nSummary generated for procurement review. Please verify details before approval.")

    return "\n".join(summary_lines)
