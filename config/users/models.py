from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None  # Удаляем поле username
    email = models.EmailField(unique=True, verbose_name='Почта')

    phone = models.CharField(max_length=35, verbose_name='Телефон', blank=True, null=True)
    city = models.CharField(max_length=100, verbose_name='Город', blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватарка', blank=True, null=True)

    USERNAME_FIELD = "email"  # Поле для логина
    REQUIRED_FIELDS = []  # Убираем обязательные поля, кроме email
