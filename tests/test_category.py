def test_str_category(sample_category, sample_product1, sample_product2):
    sample_category.add_product(sample_product1)
    sample_category.add_product(sample_product2)
    expected_str = "Product 1, 3 шт. Общее количество товаров на складе: 3"

    assert str(sample_category) == expected_str
