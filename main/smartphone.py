from main.product import Product


class Smartphone(Product):
    """Класс наследник класса Product"""

    def __init__(self, name, description, price, efficiency, model, memory, color, quantity=None):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
