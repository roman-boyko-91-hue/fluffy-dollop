class Product:
    """Наименование класса"""
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity=None):
        """Инициализация"""
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity if quantity else None


if __name__ == "__main__":
    product = Product("Samsung Galaxy C23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5
                      )
