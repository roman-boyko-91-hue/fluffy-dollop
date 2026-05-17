# Django DRF Project (CI/CD & Docker Production Ready)

Проект на Django REST Framework, полностью упакованный в Docker и
готовый к продакшну с настроенным CI/CD пайплайном.

## Стек технологий

* **Backend:** Python 3.13 / Django 5.x / Django REST Framework
* **Асинхронные задачи:** Celery / Celery Beat
* **База данных и брокер:** PostgreSQL / Redis
* **Production сервер:** Gunicorn / Nginx / Docker Compose
* **CI/CD:** GitHub Actions (Linter + Tests + Docker Build Test + Auto Deploy via SSH)

---

## Ссылка на Pull Request

* **Pull Request:** https://github.com/roman-boyko-91-hue/fluffy-dollop/pull/32
* **Адрес сервера:** http://111.88.156.28

## Локальный запуск (Разработка)

1. Клонируйте репозиторий и перейдите в ветку домашки:
   ```bash
   git clone <https://github.com/roman-boyko-91-hue/fluffy-dollop/pull/31>
   cd <drf_project>
   git checkout final_assigment
   ```

2. Создайте локальный файл окружения `.env` на основе шаблона `.env.template`:
   ```bash
   cp .env.template .env
   ```

3. Запустите проект одной командой:
   ```bash
   docker-compose up --build
