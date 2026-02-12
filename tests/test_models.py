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


def test_product_init(sample_products):
    assert sample_products[0].name == "Ноутбук"
    assert sample_products[0].description == "Игровой ноутбук"
    assert sample_products[0].price == 80000
    assert sample_products[0].quantity == 5


def test_category_init(sample_category, sample_products):
    assert sample_category.name == "Электроника"
    assert sample_category.description == "Техника для дома и офиса"
    assert sample_category.products == [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in sample_products]


def test_category_add_product(sample_category):
    p1 = Product("Мышка", "Проводная", 2090, 15)
    sample_category.add_product(p1)
    assert len(sample_category.products) == 3
    assert sample_category.products[2] == f"{p1.name}, {p1.price} руб. Остаток: {p1.quantity} шт."


def test_new_product():
    pass