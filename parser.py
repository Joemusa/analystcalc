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

    patterns = {
        "stocking": r"(\d+\.?\d*)\s*(stores)?\s*(stock|stocking)",
        "total_stores": r"(out of|total)\s*(\d+\.?\d*)",

        "current": r"(current|this month|now)\s*(\d+\.?\d*)",
        "previous": r"(previous|last month|before|from)\s*(\d+\.?\d*)",

        "brand_sales": r"(brand|product)\s*(sales)?\s*(\d+\.?\d*)",
        "market_sales": r"(market)\s*(sales)?\s*(\d+\.?\d*)"
    }

    for role, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            # Always extract the LAST NUMERIC group safely
            for group in match.groups():
                if group and group.replace('.', '', 1).isdigit():
                    roles[role] = float(group)
                    break

    return roles


