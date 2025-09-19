# Проект модуля 14
## Инструкция по установке
1. клонирование репозитория 
``` powershell
git clone git@github.com:shk1t/skypro_m14.git
```
2. проверка poetry
``` powershell
poetry --version
```
3. установка зависимостей проекта
``` powershell
poetry install
```
4. активация окружения

`если установлен shell`
``` powershell
poetry shell
```
`если не установлен`
``` powershell
poetry env activate
```
# Модули проекта
# main.py
## основной модуль проекта
# models.py
## Модуль содержит в себе классы Category и Product
### Класс Category
#### Свойства класса: 
1. name: str
2. description: str
3. products: list[Product]
#### Атрибуты класса: 
1. category_count: int
2. product_count: int
### Класс Product
#### Свойства класса: 
1. name: str
2. description: str
3. price: float
4. quantity: int
# utils.py
## Модуль содержит в себе функцию load_categories_from_json, которая принимает на вход путь до json-файла, и выводит список объектов классов Product и Category