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
def empty_category():
    """Фикстура для создания объекта Category."""
    return Category(name="Default Category", description="Description", product=[])


@pytest.fixture
def sample_product():
    return Product(name="Продукт", description="Описание", price=100, quantity=10)
