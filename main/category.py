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
        self.__products = products
        self.name = name
        self.description = description
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """Запись списка товаров в приватный атрибут"""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def product(self) -> str:
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
