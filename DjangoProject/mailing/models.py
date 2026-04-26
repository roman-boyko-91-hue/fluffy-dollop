from django.db import models
from django.conf import settings
from django.utils import timezone

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name='Email')
    full_name = models.CharField(max_length=255, verbose_name='Ф. И. О.')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return f"{self.full_name} ({self.email})"

    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Mailing(models.Model):
    start_time = models.DateTimeField(verbose_name='Дата и время начала')
    end_time = models.DateTimeField(verbose_name='Дата и время окончания')

    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')
    clients = models.ManyToManyField(Client, verbose_name='Получатели')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    @property
    def status(self):
        now = timezone.now()
        if now < self.start_time:
            return 'Создана'
        elif self.start_time <= now <= self.end_time:
            return 'Запущена'
        else:
            return 'Завершена'

    def __str__(self):
        return f"Рассылка {self.id} (статус: {self.status})"

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class MailingAttempt(models.Model):
    attempt_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время попытки')
    status = models.CharField(max_length=20, verbose_name='Статус')
    server_response = models.TextField(verbose_name='Ответ сервера', **NULLABLE)

    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Рассылка')

    class Meta:
        verbose_name = 'Попытка рассылки'
        verbose_name_plural = 'Попытки рассылок'
