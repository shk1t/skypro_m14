class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_dict: dict):
        pass
class Category:
    name: str
    description: str
    __products: list[Product]

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
    
    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self.__products]

    def add_product(self, product: Product):
        self.__products.append(product)
    