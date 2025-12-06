import pytest


def test_category_starts_with_no_product(empty_category):
    assert empty_category.name == "Default Category"
    assert empty_category.product == "В этой категории нет товаров"
