from main.product import Product


class Category:
    """Класс для категорий"""
    name: str
    description: str
    product: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, product=None):
        """Инициализация"""
        self.name = name
        self.description = description
        self.__product = product if product else []
        Category.category_count += 1
        Category.product_count += len(product) if product else 0

    def add_product(self, product: Product):
        """Запись списка товаров в приватный атрибут"""
        self.__product.append(product)
        Category.product_count += 1

    @property
    def product(self) -> str:
        """Геттер для вывода списка товаров в нужном формате"""
        if not self.__product:
            return "В этой категории нет товаров"

        product_list = []
        for product in self.__product:
           product_list.append(f"{"name"}, {"price"} руб. Остаток: {"quantity"} шт.\n")
        return product_list


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
