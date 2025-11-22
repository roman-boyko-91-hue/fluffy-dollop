import json
import os

from main.category import Category
from main.product import Product


def read_json(path: str) -> dict:
    new_path = os.path.abspath(path)
    with open(new_path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        return data


def object_from_json(data):
    items = []
    for category_data in data:
        products = []
        for product_data in category_data['products']:
            product = Product(
                name=product_data['name'],
                description=product_data['description'],
                price=product_data['price'],
                quantity=product_data['quantity']
            )
            products.append(product)
        category = Category(
            name=category_data['name'],
            description=category_data['description'],
            product=products
        )
        items.append(category)

    return items


if __name__ == "__main__":
    data_new = read_json(("../data/products.json"))
    items_new = object_from_json(data_new)
    print(items_new)
