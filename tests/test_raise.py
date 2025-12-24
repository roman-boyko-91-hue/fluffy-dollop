import pytest

from main.category import Category
from main.product import Product


def test_middle_category_exception_handling():
    category = Category("Смартфоны", "Категория смартфонов", [])
    try:
        assert category.middle_category() == 0
    except Exception as e:
        assert False, f"Exception was raised: {e}"


def test_product_not_quantity_raises_error():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)


def test_middle_category_no_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 1)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Категория смартфонов", [product1, product2])
    assert category.middle_category() == 195000.0


def test_negative_price_raises_value_error():
    with pytest.raises(ValueError, match="Цена не может быть отрицательной!"):
        product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", - 180000.0, 1)
