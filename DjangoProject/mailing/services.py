from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
from .models import MailingAttempt


def send_mailing(mailing):
    now = timezone.now()

    # Проверка времени
    if not (mailing.start_time <= now <= mailing.end_time):
        return {"error": "Текущее время вне диапазона рассылки"}

    # Получение данных
    subject = mailing.message.subject
    body = mailing.message.body
    clients = mailing.clients.all()

    # Отправка писем
    for client in clients:
        try:
            send_mail(
                subject=subject,
                message=body,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email],
                fail_silently=False,
            )
            status = 'Успешно'
            server_response = '200 OK'
        except Exception as e:
            status = 'Не успешно'
            server_response = str(e)

        # Сохраняем попытку
        MailingAttempt.objects.create(
            mailing=mailing,
            status=status,
            server_response=server_response
        )
    return {"success": True}
