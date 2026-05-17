FROM python:3.13-slim

WORKDIR /app

# Настройки Python для Docker
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Сначала копируем и ставим зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Статикf Django для Nginx
RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Запускаем приложение через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "drf_project.wsgi:application"]
