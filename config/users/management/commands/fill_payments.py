from django.core.management import BaseCommand
from materials.models import Course, Lesson
from users.models import Payment, User


class Command(BaseCommand):
    help = 'Заполняет базу данных тестовыми платежами'

    def handle(self, *args, **options):
        # 1. Очистка от старых платежей, чтобы не дублировать при повторном запуске
        Payment.objects.all().delete()

        # 2. Находим или создаем пользователя и объекты для привязки
        user = User.objects.first()
        course = Course.objects.first()
        lesson = Lesson.objects.first()

        if not user or not course:
            self.stdout.write(self.style.ERROR('Сначала создайте пользователя и курс через админку!'))
            return

        # 3. Создаем список объектов платежей
        payments_list = [
            {
                "user": user,
                "paid_course": course,
                "amount": 15000.50,
                "payment_method": "transfer"
            },
            {
                "user": user,
                "paid_lesson": lesson,
                "amount": 1500.00,
                "payment_method": "cash"
            }
        ]

        # 4. Сохраняем их в базу
        for payment_data in payments_list:
            Payment.objects.create(**payment_data)

        self.stdout.write(self.style.SUCCESS('Платежи успешно добавлены!'))
