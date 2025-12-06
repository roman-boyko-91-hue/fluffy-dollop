import pytest

from main.category import Category
from main.product import Product


@pytest.fixture
def product():
    return Product(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни",
        product=[
            {
                "name": "Samsung Galaxy C23 Ultra",
                "description": "256GB, Серый цвет, 200MP камера",
                "price": 180000.0,
                "quantity": 5
            },
            {"name": "Iphone 15",
             "description": "512GB, Gray space",
             "price": 210000.0,
             "quantity": 8}]
    )


@pytest.fixture
def price():
    return Product(
        "Samsung Galaxy C23 Ultra",
        "256GB, Серый цвет, 200MP камера",
        180000.0,
        5
    )
