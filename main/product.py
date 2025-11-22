class Product:
    """Класс Продукты"""
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity=None):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity if quantity else None


if __name__ == "__main__":
    product = Product()
