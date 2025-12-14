import pytest
from main.product import Product


@pytest.fixture
def sample_product1():
    return Product(name="Product 1", price=100, description="description")


@pytest.fixture
def sample_product2():
    return Product(name="Product 2", price=200, description="description")
