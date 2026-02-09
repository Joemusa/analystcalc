def numeric_distribution(stores_stocking: int, total_stores: int):
    if total_stores == 0:
        return None

    result = (stores_stocking / total_stores) * 100

    return {
        "metric": "Numeric Distribution",
        "formula": "(Stores Stocking / Total Stores) × 100",
        "inputs": {
            "stores_stocking": stores_stocking,
            "total_stores": total_stores
        },
        "calculation": f"({stores_stocking} / {total_stores}) × 100",
        "result": round(result, 2),
        "unit": "%"
    }
  
def market_share(brand_sales: float, total_market_sales: float):
    if total_market_sales == 0:
        return None

    result = (brand_sales / total_market_sales) * 100

    return {
        "metric": "Market Share",
        "formula": "(Brand Sales / Total Market Sales) × 100",
        "inputs": {
            "brand_sales": brand_sales,
            "total_market_sales": total_market_sales
        },
        "calculation": f"({brand_sales} / {total_market_sales}) × 100",
        "result": round(result, 2),
        "unit": "%"
    }

def contribution(part_value: float, total_value: float):
    if total_value == 0:
        return None

    result = (part_value / total_value) * 100

    return {
        "metric": "Contribution",
        "formula": "(Part Value / Total Value) × 100",
        "inputs": {
            "part_value": part_value,
            "total_value": total_value
        },
        "calculation": f"({part_value} / {total_value}) × 100",
        "result": round(result, 2),
        "unit": "%"
    }
