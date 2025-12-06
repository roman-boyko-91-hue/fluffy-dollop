def test_product(product):
    assert product.name == "Samsung Galaxy C23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter_positive(sample_product):
    sample_product.price = 50
    assert sample_product.price == 50


def test_price_setter_negative(sample_product):
    sample_product.price = -10
    assert sample_product.price == 100
