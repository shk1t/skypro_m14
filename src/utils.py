import json

from models import Category, Product


def load_categories_from_json(path_str: str) -> list[Category]:
    with open(path_str, "r", encoding="utf-8") as f:
        data = json.load(f)

    categories = []
    for cat_data in data:
        products = [Product(p["name"], p["description"], p["price"], p["quantity"]) for p in cat_data["products"]]
        category = Category(cat_data["name"], cat_data["description"], products)
        categories.append(category)

    return categories
