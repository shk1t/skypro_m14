class Product:
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> str:
        """Геттер для получения цены продукта"""
        return f"{self.name}. Цена: {self.__price}"

    @price.setter
    def price(self, price: float) -> None:
        """Сеттер для присваивания новой цены продукта"""
        if price > 0:
            if price < self.__price:
                agreement = input("Понизить цену? Да[y] Нет[n]")
                self.__price = price if agreement == "y" else self.__price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    @classmethod
    def new_product(cls, product_dict: dict) -> "Product":
        """Класс-метод, с помощью которого можно инициализировать новый объект класса Product"""
        return cls(
            name=product_dict["name"],
            description=product_dict["description"],
            price=product_dict["price"],
            quantity=product_dict["quantity"],
        )


class Category:
    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self) -> list[str]:
        """Геттер для получения списка продуктов с их данными"""
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n" for product in self.__products]

    def add_product(self, product: Product) -> None:
        """Функция для добавления продукта в категорию"""
        self.__products.append(product)
        Category.product_count += 1
