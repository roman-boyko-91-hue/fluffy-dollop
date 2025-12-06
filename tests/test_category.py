from tests.conftest import category, product, price


def test_price_normal(category):
    """Проверка ценового значения"""
    assert price == 180000.0
