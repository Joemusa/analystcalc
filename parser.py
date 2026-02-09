import re

def extract_numbers(text: str):
    """
    Extract all numbers from text.
    Returns a list of floats.
    """
    numbers = re.findall(r"\d+\.?\d*", text)
    return [float(n) for n in numbers]


def detect_metric(text: str):
    """
    Detect which metric the user is asking for.
    """
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
