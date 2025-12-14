from typing import Any
from product import Product


class LawnGrass(Product):
    """Класс наследник класса Product"""
    def __init__(self, name, description, price, quantity=None, country=Any, germination_period=Any, color=Any):
        super().__init__(name, description, price, quantity)
        self.efficiency = country
        self.model = germination_period
        self.color = color
