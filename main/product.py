from main.baseproduct import BaseProduct
from main.mixin_print import MixinPrint


class Product(BaseProduct, MixinPrint):
    """Наименование класса"""
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity=0):
        """Инициализация"""

        self.name = name
        self.description = description
        if price < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.__price = float(price)
        if quantity > 0:
            self.quantity = int(quantity)
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product или его наследники")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __repr__(self):
        """Метод для информативного отображения"""
        return f"Product({self.name}, {self.description}, {self.price}, {self.quantity})"

    @classmethod
    def new_product(cls, name, description, quantity, price):
        instance = cls(name, description, quantity)
        instance.price = price
        return instance

    def base_product(cls, *args, **kwargs):
        pass

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
