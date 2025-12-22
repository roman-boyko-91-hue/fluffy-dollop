import os
import sys

import pytest

from main.product import Product

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def fix_product1():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def product_5():
    return Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
