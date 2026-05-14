# Трекер привычек (Django DRF + Docker)

Курсовой проект № 5 - созданию API-сервиса 
для отслеживания полезных привычек. 

## Технологический стек
* Python 3.13
* Django 6.0.5 / Django REST Framework (DRF)
* PostgreSQL
* Redis (Брокер сообщений)
* Celery & Celery Beat (Фоновые и периодические задачи)
* Docker / Docker Compose

## Как запустить проект в Docker

### 1. Клонируйте репозиторий и перейдите в ветку домашней работы:
```bash
git checkout homework_34_2
```

### 2. Создайте файл окружения `.env` в корне проекта:
```env
DEBUG=True
SECRET_KEY=your_secret_key
POSTGRES_DB=your_db_name
POSTGRES_USER=your_db_user
POSTGRES_PASSWORD=your_db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
```

### 3. Соберите и запустите контейнеры:
```bash
docker-compose up --build
```

После этого автоматически запустятся 5 сервисов: 
Django (`web`), PostgreSQL (`db`), Redis (`redis`), а 
также воркер и планировщик Celery.

### 4. Примените миграции (в новом окне терминала):
```bash
docker-compose exec web python manage.py migrate
```

## 📖 Документация API
После запуска проекта документация Swagger доступна по адресу:
* http://localhost:8000/swagger/
* http://localhost:8000/redoc/
