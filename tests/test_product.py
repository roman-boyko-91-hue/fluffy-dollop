from main.product import Product


def test_product_attribute_change():
    product = Product(name="iPhone 14", description="128GB, Черный цвет", price=150000.0, quantity=10)
    product.price = 140000.0
    assert product.price == 140000.0

def test_product_attribute_modification():
    product = Product("Samsung", "64GB", 50000.0, 3)
    product.price = 55000.0
    assert product.price == 55000.0
    product.quantity = 4
    assert product.quantity == 4
