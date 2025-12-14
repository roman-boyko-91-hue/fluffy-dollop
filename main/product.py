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
        self.__price = price
        self.quantity = quantity if quantity else None

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) in Product:
            return (self.price * self.quantity) + (other.price * other.quantity)

    raise TypeError

    def __repr__(self):
        """Метод для информативного отображения"""
        return f"Product({self.name}, {self.description}, {self.price}, {self.quantity})\n"

    @classmethod
    def new_product(cls, product_dict):
        return cls(**product_dict)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price


if __name__ == "__main__":
    product = Product("Samsung Galaxy C23 Ultra",
                      "256GB, Серый цвет, 200MP камера",
                      180000.0,
                      5
                      )
