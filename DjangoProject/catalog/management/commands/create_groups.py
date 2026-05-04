from django.core.management import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу модераторов и назначает права доступа'

    def handle(self, *args, **options):
        # 1. Создаем группу
        moderator_group, created = Group.objects.get_or_create(name='Модератор')

        # 2. Получаем тип контента для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # 3. Список кодов разрешений, которые нужно дать модератору
        # can_unpublish_product — кастомное право из Meta модели
        # delete_product — стандартное право на удаление любого товара
        # change_product — стандартное право на редактирование
        permissions_list = [
            'can_unpublish_product',
            'delete_product',
            'change_product',
        ]

        # 4. Находим каждое право в БД и добавляем в группу
        for perm_codename in permissions_list:
            try:
                permission = Permission.objects.get(
                    codename=perm_codename,
                    content_type=content_type
                )
                moderator_group.permissions.add(permission)
            except Permission.DoesNotExist:
                self.stdout.write(self.style.ERROR(f'Право {perm_codename} не найдено в базе.'))

        if created:
            self.stdout.write(self.style.SUCCESS('Группа "Модератор" успешно создана и настроена'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модератор" уже существует, права обновлены'))
