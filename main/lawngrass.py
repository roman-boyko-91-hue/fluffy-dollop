from product import Product


class LawnGrass(Product):
    """Класс наследник класса Product"""
    def __init__(self, name, description, price, country, germination_period, color, quantity=None):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
