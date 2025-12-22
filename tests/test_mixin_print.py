from main.product import Product


def test_product_repr_output(capsys):
    """Проверяем, что repr возвращает ожидаемую строку"""
    Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_product_repr():
    """Проверяем, что repr возвращает ожидаемую строку"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    expected_repr = "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"
    assert repr(product) == expected_repr


def test_repr_and_recreation(product_5):
    """Проверяем, что repr возвращает ожидаемую строку"""
    expected_repr = "Product(Xiaomi Redmi Note 11, 1024GB, Синий, 31000.0, 14)"
    assert repr(product_5) == expected_repr


def test_repr_with_negative_values():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", -180000.0, -5)
    expected_repr = "Product(Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, -180000.0, -5)"
    assert repr(product) == expected_repr


def test_repr_with_zero_and_max_values():
    """Тестирование"""
    product = Product("Iphone 15", "512GB, Gray space", float('inf'), int(1e6))
    expected_repr = "Product(Iphone 15, 512GB, Gray space, inf, 1000000)"
    assert repr(product) == expected_repr
