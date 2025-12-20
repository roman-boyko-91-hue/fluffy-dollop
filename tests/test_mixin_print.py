from main.lawngrass import LawnGrass
from main.product import Product


def test_product_repr_output(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_product_attribute_change():
    product = Product(name="iPhone 14", description="128GB, Черный цвет", price=150000.0, quantity=10)
    product.price = 140000.0
    assert product.price == 140000.0
