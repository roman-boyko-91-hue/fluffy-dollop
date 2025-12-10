import pytest
from main.product import Product


def test_product_str():
    """Тест проверяет, что метод __str__ возвращает ожидаемую строку"""
    product = Product(name="Test Product", description="Test Description", price=100, quantity=5)
    expected_str = "Test Product, 100 руб. Остаток: 5 шт."
    assert str(product) == expected_str


def test_product_add():
    """Сумма (через метод __add__) равна ожидаемому значению"""
    product1 = Product(name="Product 1", description="Description 1", price=100, quantity=2)
    product2 = Product(name="Product 2", description="Description 2", price=150, quantity=3)
    expected_total = (100 * 2) + (150 * 3)
    assert product1 + product2 == expected_total
