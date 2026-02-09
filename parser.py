def extract_number_roles(text: str):
    import re
    text = text.lower()
    roles = {}

    # 1️⃣ Numeric distribution patterns
    stocking_match = re.search(
        r"(\d+\.?\d*)\s*(stores)?\s*(stock|stocking)",
        text
    )
    if stocking_match:
        roles["stocking"] = float(stocking_match.group(1))

    total_match = re.search(
        r"out of\s*(\d+\.?\d*)|total\s*(\d+\.?\d*)",
        text
    )
    if total_match:
        roles["total_stores"] = float(
            total_match.group(1) or total_match.group(2)
        )

    # 2️⃣ Growth patterns
    current_match = re.search(
        r"(current|this month|now)\s*(\d+\.?\d*)",
        text
    )
    if current_match:
        roles["current"] = float(current_match.group(2))

    previous_match = re.search(
        r"(previous|last month|before|from)\s*(\d+\.?\d*)",
        text
    )
    if previous_match:
        roles["previous"] = float(previous_match.group(2))

    # 3️⃣ Market share patterns
    brand_match = re.search(
        r"brand\s*(sales)?\s*(\d+\.?\d*)",
        text
    )
    if brand_match:
        roles["brand_sales"] = float(brand_match.group(2))

    market_match = re.search(
        r"market\s*(sales)?\s*(\d+\.?\d*)",
        text
    )
    if market_match:
        roles["market_sales"] = float(market_match.group(2))

    return roles
