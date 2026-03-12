# Интернет-магазин: модели товаров и категорий

Учебный проект на Python, в котором реализованы базовые сущности интернет-магазина:

- Product — товар;
- Category — категория товаров;
- загрузка данных из JSON;
- тесты на pytest.

Проект демонстрирует работу с:

- классами и объектами;
- инкапсуляцией и свойствами (`@property`);
- магическими методами __str__ и __add__;
- classmethod;
- чтением JSON-файлов;
- автоматическим тестированием.

## Функциональность

### Класс Product
Класс описывает отдельный товар и содержит:

- название товара;
- описание;
- цену;
- количество на складе.

Реализовано:

- создание объекта товара;
- строковое представление товара;
- сложение двух товаров через +;
- геттер и сеттер для цены;
- создание товара из словаря через new_product().

Пример:
from src.models import Product

product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5)
print(product)

Результат:
Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.

### Класс Category
Класс описывает категорию товаров и содержит:

- название категории;
- описание категории;
- список товаров.

Также используются атрибуты класса:

- category_count — количество созданных категорий;
- product_count — общее количество товаров во всех категориях.

Реализовано:

- создание категории со списком товаров;
- получение строкового представления категории;
- получение списка товаров через свойство products;
- добавление нового товара в категорию.

Пример:
from src.models import Category, Product

product1 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product2 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

category = Category(
    "Смартфоны",
    "Смартфоны и аксессуары",
    [product1, product2]
)

print(category)
print(category.products)

## Загрузка данных из JSON

В модуле src/utils.py реализована функция load_categories_from_json(path_str: str), которая:

1. принимает путь к JSON-файлу;
2. считывает данные;
3. создает объекты Product и Category;
4. возвращает список категорий.

Пример использования:
from src.utils import load_categories_from_json

categories = load_categories_from_json("data/products.json")
for category in categories:
    print(category)

## Структура проекта
skypro-m14/
├── data/
│   └── products.json        # исходные данные о товарах
├── src/
│   ├── main.py              # точка входа для ручной проверки
│   ├── models.py            # классы Product и Category
│   ├── utils.py             # загрузка данных из JSON
│   └── __init__.py
├── tests/
│   ├── test_models.py       # тесты моделей
│   ├── test_utils.py        # тесты загрузки JSON
│   └── __init__.py
├── pyproject.toml           # зависимости и настройки проекта
└── README.md

## Установка и запуск

### 1. Клонирование репозитория
git clone <URL_репозитория>
cd skypro-m14

### 2. Установка Poetry

Проверьте, установлен ли Poetry:
poetry --version

### 3. Установка зависимостей
poetry install

### 4. Активация виртуального окружения

Если установлен плагин shell:
poetry shell

Либо:
poetry env activate

## Запуск проекта

Запуск демонстрационного сценария:
python src/main.py

## Запуск тестов
pytest

Запуск тестов с покрытием:
pytest --cov=src --cov-report=term-missing

## Используемые технологии

- Python 3.13+
- Poetry
- Pytest
- Pytest-cov
- Flake8
- Black
- isort
- mypy
