from typing import Any

from main.product import Product


class Smartphone(Product):
    """Класс наследник класса Product"""

    def __init__(self, name, description, price, quantity=None, efficiency=Any, model=Any, memory=Any, color=Any):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
