from abc import ABC, abstractmethod


class BaseProduct(ABC):

    @classmethod
    @abstractmethod
    def base_product(cls, *args, **kwargs):
        pass
