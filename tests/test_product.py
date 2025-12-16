from main.lawngrass import LawnGrass
from main.smartphone import Smartphone


def test_smartphone_product_init():
    """Проверка атрибутов"""
    smartphone_product = Smartphone("name", "description", 200,
                                    "efficiency", "model", "memory", "Color", 1)


def test_lamngrass_init():
    """Проверка атрибутов"""
    lawn_grass = LawnGrass("name", "description", 100.0,
                           "country", "period", "color")


def test_smartphone_product_add(smartphone_product1, smartphone_product2):
    assert (smartphone_product1 + smartphone_product2 == (smartphone_product1.__price * smartphone_product1.quantity) +
            (smartphone_product2.__price * smartphone_product2.quantity))
