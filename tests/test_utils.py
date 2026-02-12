import json
import tempfile
import os

from src.models import Category, Product
from src.utils import load_categories_from_json


def test_load_categories_from_json():
    data = [
        {
            "name": "Фрукты",
            "description": "Свежие фрукты",
            "products": [{"name": "Яблоко", "description": "Зелёное", "price": 50, "quantity": 10}],
        }
    ]

    tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json", mode="w", encoding="utf-8")
    json.dump(data, tmp_file, ensure_ascii=False)
    tmp_file.close()

    categories = load_categories_from_json(tmp_file.name)

    assert len(categories) == 1
    cat = categories[0]
    assert isinstance(cat, Category)
    assert cat.name == "Фрукты"
    assert cat.description == "Свежие фрукты"
    assert len(cat.products) == 1

    os.remove(tmp_file.name)
