from main.product import Product


def test_product_repr_output(capsys):
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_product_repr():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    expected_repr = "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    assert repr(product) == expected_repr


def test_repr_and_recreation(product_5):
    # Проверяем, что repr возвращает ожидаемую строку
    expected_repr = "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
    assert repr(product_5) == expected_repr
