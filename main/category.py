from main.product import Product


class Category:
    """Класс для категорий"""
    name: str
    description: str
    product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация"""
        self.__products = products if products is not None else []
        self.name = name
        self.description = description

    def __str__(self):
        all_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, общее количество продуктов: {all_quantity} шт."

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер для вывода списка товаров в нужном формате"""
        if not self.__products:
            return "В этой категории нет товаров"

        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_list)


if __name__ == "__main__":
    product_1 = Product("Samsung Galaxy C23 Ultra",
                        "256GB, Серый цвет, 200MP камера",
                        180000.0,
                        5
                        )
    product_2 = Product("Iphone 15",
                        "512GB, Gray space",
                        210000.0,
                        8
                        )

    сategory = Category("name", "description", [product_1, product_2])
