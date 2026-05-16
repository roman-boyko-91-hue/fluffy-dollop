FROM python:3.13

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

FROM python:3.11

# Ставим рабочую директорию
WORKDIR /app

# Копируем и ставим зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Собираем статику Django для Nginx
RUN python manage.py collectstatic --noinput

# Запускаем приложение через Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "drf_project.wsgi:application"]
