import pytest

import sys
import os

from main.lawngrass import LawnGrass
from main.smartphone import Smartphone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def smartphone_product1():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


@pytest.fixture
def smartphone_product2():
    return Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024,
                      "Синий")


@pytest.fixture
def lamngrass_test_1():
    return LawnGrass("Газонная трава", "Элитная трава для газона",
                     500.0, 20, "Россия", "7 дней", "Зеленый")


def lamngrass_test_2():
    return LawnGrass("Газонная трава 2", "Выносливая трава",
                     450.0, 15, "США", "5 дней", "Темно-зеленый")
