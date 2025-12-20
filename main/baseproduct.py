from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс"""

    def __init__(self, name: str, description: str, quantity: int) -> None:
        """Инициализация продукта."""
        self.name = name
        self.description = description
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass
