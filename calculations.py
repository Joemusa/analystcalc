def numeric_distribution(stores_stocking, total_stores):
    if total_stores == 0:
        return None

    value = (stores_stocking / total_stores) * 100

    return {
        "metric": "Numeric Distribution",
        "formula": "Stores Stocking ÷ Total Stores × 100",
        "calculation": f"{stores_stocking} ÷ {total_stores} × 100",
        "result": round(value, 2),
        "unit": "%"
    }


def market_share(brand_sales, total_market_sales):
    if total_market_sales == 0:
        return None

    value = (brand_sales / total_market_sales) * 100

    return {
        "metric": "Market Share",
        "formula": "Brand Sales ÷ Total Market Sales × 100",
        "calculation": f"{brand_sales} ÷ {total_market_sales} × 100",
        "result": round(value, 2),
        "unit": "%"
    }


def contribution(part_value, total_value):
    if total_value == 0:
        return None

    value = (part_value / total_value) * 100

    return {
        "metric": "Contribution",
        "formula": "Part ÷ Total × 100",
        "calculation": f"{part_value} ÷ {total_value} × 100",
        "result": round(value, 2),
        "unit": "%"
    }


def growth(current, previous):
    if previous == 0:
        return None

    value = ((current - previous) / previous) * 100

    return {
        "metric": "Growth",
        "formula": "(Current − Previous) ÷ Previous × 100",
        "calculation": f"({current} − {previous}) ÷ {previous} × 100",
        "result": round(value, 2),
        "unit": "%"
    }

