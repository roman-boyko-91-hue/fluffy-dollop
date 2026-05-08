from datetime import timedelta

from celery import shared_task
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.utils import timezone

from config import settings
from materials.models import Subscription


@shared_task
def send_course_update_email(course_id, course_name):
    # Ищем все подписки на этот курс
    subscriptions = Subscription.objects.filter(course_id=course_id).select_related('user')

    # Собираем список email-адресов подписчиков
    recipient_list = [sub.user.email for sub in subscriptions if sub.user.email]

    if recipient_list:
        send_mail(
            subject=f"Обновление курса: {course_name}",
            message=f"Привет! В курсе '{course_name}' появились новые материалы. Заходи скорее!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=recipient_list,
            fail_silently=False,
        )


@shared_task
def block_inactive_users():
    User = get_user_model()
    # Определяем порог в 30 дней
    month_ago = timezone.now() - timedelta(days=30)

    # Ищем пользователей: не заходили > 30 дней, активны и НЕ админы
    inactive_users = User.objects.filter(
        last_login__lt=month_ago,
        is_active=True,
        is_superuser=False
    )

    # Обновление флага
    count = inactive_users.update(is_active=False)

    if count > 0:
        print(f"Celery Beat: Заблокировано неактивных пользователей: {count}")
    else:
        print("Celery Beat: Неактивных пользователей для блокировки не найдено.")
