import re

def detect_metric(question):

    question = question.lower()

    # 🔹 Always check more specific terms first
    if "weighted distribution" in question:
        return "Weighted Distribution"

    if "numeric distribution" in question:
        return "Numeric Distribution"

    if "growth" in question:
        return "Growth"

    if "market share" in question:
        return "Market Share"

    if "contribution" in question:
        return "Contribution"

    return None


def extract_number_roles(text: str):
    text = text.lower()
    roles = {}

    # Numeric Distribution
    m = re.search(r"(\d+\.?\d*)\s*(stores)?\s*(stock|stocking)", text)
    if m:
        roles["stocking"] = float(m.group(1))

    m = re.search(r"out of\s*(\d+\.?\d*)|total\s*(\d+\.?\d*)", text)
    if m:
        roles["total_stores"] = float(m.group(1) or m.group(2))

    # Growth
    m = re.search(r"(current|this month|now)\s*(\d+\.?\d*)", text)
    if m:
        roles["current"] = float(m.group(2))

    m = re.search(r"(previous|last month|before|from)\s*(\d+\.?\d*)", text)
    if m:
        roles["previous"] = float(m.group(2))

    # Market Share
    m = re.search(r"brand\s*(sales)?\s*(\d+\.?\d*)", text)
    if m:
        roles["brand_sales"] = float(m.group(2))

    m = re.search(r"market\s*(sales)?\s*(\d+\.?\d*)", text)
    if m:
        roles["market_sales"] = float(m.group(2))

    return roles

