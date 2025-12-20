from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс"""

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
