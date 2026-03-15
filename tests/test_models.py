import pytest

from src.models import Category, Product


@pytest.fixture(autouse=True)
def reser_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture()
def sample_products():
    p1 = Product("Ноутбук", "Игровой ноутбук", 80000, 5)
    p2 = Product("Мышка", "Беспроводная", 2000, 15)
    return [p1, p2]


@pytest.fixture()
def sample_category(sample_products):
    return Category("Электроника", "Техника для дома и офиса", sample_products)


def test_product(sample_products, capsys, monkeypatch):
    assert sample_products[0].name == "Ноутбук"
    assert sample_products[0].description == "Игровой ноутбук"
    assert sample_products[0].price == f"{sample_products[0].name}. Цена: 80000"
    assert str(sample_products[0]) == "Ноутбук, 80000 руб. Остаток: 5 шт."
    assert sample_products[0] + sample_products[1] == 80000 * 5 + 2000 * 15
    sample_products[0].price = -1
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_products[0].price = 79000
    assert sample_products[0].price == f"{sample_products[0].name}. Цена: 80000"

    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_products[0].price = 79000
    assert sample_products[0].price == f"{sample_products[0].name}. Цена: 79000"

    assert sample_products[0].quantity == 5


def test_category_init(sample_category, sample_products):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома и офиса"
    assert str(sample_category) == "Электроника, количество продуктов: 2 шт."
    assert sample_category.products == [
        f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in sample_products
    ]


def test_category_add_product(sample_category):
    p1 = Product("Мышка", "Проводная", 2090, 15)
    sample_category.add_product(p1)

    with pytest.raises(TypeError):
        sample_category.add_product("не продукт")
    assert len(sample_category.products) == 3
    assert sample_category.products[2] == f"{p1.name}, {p1.price} руб. Остаток: {p1.quantity} шт.\n"


def test_new_product():
    p1 = Product.new_product({"name": "Мышка", "description": "Проводная", "price": 2090, "quantity": 14})
    assert p1.name == "Мышка"
    assert p1.description == "Проводная"
    assert p1.price == f"{p1.name}. Цена: 2090"
    assert p1.quantity == 14
