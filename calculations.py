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

def metric_guide(metric):

    guides = {

        "Numeric Distribution": {
            "formula": "Numeric Distribution (%) = (Stores Stocking ÷ Total Stores) × 100",
            "explanation": "Numeric Distribution measures how widely a product is available across the market. It reflects distribution reach, not sales performance.",
            "example_values": (120, 400)
        },

        "Market Share": {
            "formula": "Market Share (%) = (Brand Sales ÷ Total Market Sales) × 100",
            "explanation": "Market Share indicates the percentage of total category sales captured by the brand.",
            "example_values": (50000, 200000)
        },

        "Contribution": {
            "formula": "Contribution (%) = (Part Value ÷ Total Value) × 100",
            "explanation": "Contribution shows the relative importance of a product within a portfolio.",
            "example_values": (30000, 150000)
        },

        "Growth": {
            "formula": "Growth (%) = ((Current - Previous) ÷ Previous) × 100",
            "explanation": "Growth measures percentage increase or decrease between two periods.",
            "example_values": (100000, 80000)
        }

    }

    return guides.get(metric, None)
