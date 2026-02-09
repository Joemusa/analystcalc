import re

def detect_metric(text: str):
    text = text.lower()

    if "numeric distribution" in text or "distribution" in text:
        return "Numeric Distribution"

    if "market share" in text or "share" in text:
        return "Market Share"

    if "growth" in text or "increase" in text or "decline" in text:
        return "Growth"

    if "contribution" in text:
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

