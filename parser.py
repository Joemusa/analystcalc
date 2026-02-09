import re

def extract_number_roles(text: str):
    text = text.lower()

    roles = {}

    patterns = {
        "current": r"(current|this month|now)\s*(\d+\.?\d*)",
        "previous": r"(previous|last month|before|from)\s*(\d+\.?\d*)",
        "stocking": r"(\d+\.?\d*)\s*(stores)?\s*(stock|stocking)",
        "total_stores": r"(out of|total)\s*(\d+\.?\d*)",
        "brand_sales": r"(brand|product)\s*(sales)?\s*(\d+\.?\d*)",
        "market_sales": r"(market)\s*(sales)?\s*(\d+\.?\d*)"
    }

    for role, pattern in patterns.items():
        match = re.search(pattern, text)
        if match:
            roles[role] = float(match.groups()[-1])

    return roles

