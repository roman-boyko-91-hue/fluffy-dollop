from django.core.management import BaseCommand
from catalog.models import Category, Product
from users.models import User


class Command(BaseCommand):
    help = 'Удаляет старые данные и заполняет базу тестовыми категориями и продуктами'

    def handle(self, *args, **options):
        # 1. Удаление данных (сначала продукты, потом категории из-за связей)
        user = User.objects.first()
        Product.objects.all().delete()
        Category.objects.all().delete()

        # 2. Создание категорий
        electronics = Category.objects.create(name='Электроника', description='Гаджеты')
        clothing = Category.objects.create(name='Одежда', description='Вещи')

        # 3. Список продуктов для добавления
        product_list = [
            {'name': 'Ноутбук', 'price': 150000, 'category': electronics},
            {'name': 'Смартфон', 'price': 80000, 'category': electronics},
            {'name': 'Худи', 'price': 4500, 'category': clothing},
            {'name': 'Джинсы', 'price': 6000, 'category': clothing},
        ]

        # 4. Создание объектов продуктов
        products_for_create = []
        for product_item in product_list:
            Product.objects.create(**product_item, owner=user)

        # Массовое создание для оптимизации
        Product.objects.bulk_create(products_for_create)

        self.stdout.write(self.style.SUCCESS('База данных успешно очищена и заполнена тестовыми данными!'))
