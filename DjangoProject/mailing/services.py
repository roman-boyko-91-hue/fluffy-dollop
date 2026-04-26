from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from .models import MailingAttempt


def send_mailing(mailing):
    now = timezone.now()
    if not (mailing.start_time <= now <= mailing.end_time):
        return {"error": "Вне диапазона времени"}

    clients = mailing.clients.all()
    # Список для сбора объектов
    attempts_to_create = []

    for client in clients:
        try:
            send_mail(
                subject=mailing.message.subject,
                message=mailing.message.body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email]
            )
            status, response = 'Успешно', '200 OK'
        except Exception as e:
            status, response = 'Не успешно', str(e)

        # Создаем объект в памяти, но не сохраняем в БД (.create() не вызываем)
        attempts_to_create.append(
            MailingAttempt(
                mailing=mailing,
                status=status,
                server_response=response
            )
        )

    # Сохраняем всё одним запросом
    MailingAttempt.objects.bulk_create(attempts_to_create)
    return {"success": True}
