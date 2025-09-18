import pytest
from src.main import Category, Product


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
    assert sample_category.products == sample_products


def test_category_attributes(sample_category, sample_products):
    assert Category.category_count == 1
    assert Category.product_count == 2

    p3 = Product("Клавиатура", "Механическая", 5000, 10)
    cat2 = Category("Переферия", "Комплектующие", [p3])

    assert Category.category_count == 2
    assert Category.product_count == 3
