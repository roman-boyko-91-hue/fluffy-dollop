from lawngrass import LawnGrass
from smartphone import Smartphone


def test_smartphone_product_init():
    """Проверка атрибутов"""
    smartphone_product = Smartphone("name", "description", "price", "memory", "model", "color")


def test_lamngrass_init():
    """Проверка атрибутов"""
    lawn_grass = LawnGrass("name", "description", 100.0, "country", "period", "color")


def test_smartphone_product_add(smartphone_product1, smartphone_product2):
    assert (smartphone_product1 + smartphone_product2 == (smartphone_product1.__price * smartphone_product1.quantity) +
            (smartphone_product2.__price * smartphone_product2.quantity))
