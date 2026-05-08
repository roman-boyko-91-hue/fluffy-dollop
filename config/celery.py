from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Указываем настройки Django для Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Создаем экземпляр Celery (обычно называют по имени папки проекта)
app = Celery('config')

# Читаем настройки из settings.py, префикс CELERY_ обязателен
app.config_from_object('django.conf:settings', namespace='CELERY')

# Автоматический поиск задач в файлах tasks.py приложений
app.autodiscover_tasks()
