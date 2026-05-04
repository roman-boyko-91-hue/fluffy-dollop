from django.core.cache import cache
from django.conf import settings
from .models import Product


def get_products_by_category(category_id):
    """Возвращает список продуктов конкретной категории с кешированием"""
    if not settings.CACHE_ENABLED:
        return Product.objects.filter(category_id=category_id)

    key = f'products_list_{category_id}'
    products = cache.get(key)

    if products is None:
        products = Product.objects.filter(category_id=category_id)
        cache.set(key, products)

    return products
