# Django DRF Project (CI/CD & Docker Production Ready)

Проект на Django REST Framework, полностью упакованный в Docker и 
готовый к продакшну с настроенным CI/CD пайплайном.

## Стек технологий
* **Backend:** Python 3.13 / Django 5.x / Django REST Framework
* **Асинхронные задачи:** Celery / Celery Beat
* **База данных и брокер:** PostgreSQL / Redis
* **Production сервер:** Gunicorn / Nginx / Docker Compose
* **CI/CD:** GitHub Actions (Linter + Tests + Auto Deploy via SSH)

---

## Ссылка на Pull Request
* **Pull Request:** https://github.com/roman-boyko-91-hue/fluffy-dollop/pull/31

---

## Архитектура контейнеров (Docker Compose)
Вся инфраструктура разделена на изолированные сервисы:
* `web` — Django-приложение (запускается через Production-сервер Gunicorn, порт 8000 закрыт от внешнего мира и доступен только внутри сети Docker).
* `db` — База данных PostgreSQL 15 с автоматическим хелсчеком.
* `redis` — Брокер сообщений для Celery.
* `celery` / `celery_beat` — Воркеры для обработки фоновых и периодических задач.
* `nginx` — Единственная точка входа (Reverse Proxy), которая принимает внешний трафик на 80 порту и раздает статику.

---

## Локальный запуск (Разработка)

1. Клонируйте репозиторий и перейдите в ветку домашки:
   ```bash
   git clone <https://github.com/roman-boyko-91-hue/fluffy-dollop/pull/31>
   cd <drf_project>
   git checkout homework_35_2
   ```

2. Создайте локальный файл окружения `.env` на основе шаблона `.env.template`:
   ```bash
   cp .env.template .env
   ```
   *Убедитесь, что для работы внутри Docker переменная `CELERY_BROKER_URL` установлена в значение `redis://redis:6379/0`.*

3. Запустите проект одной командой:
   ```bash
   docker-compose up --build
   ```
   *Все миграции применятся автоматически, статика соберется, а сервисы запустятся в правильном порядке благодаря `depends_on`.*

---

## Описание CI/CD пайплайна (.github/workflows/ci.yml)

Пайплайн разделен на три изолированные и последовательные стадии:
1. **Lint (Flake8):** Автоматическая проверка кода на синтаксические ошибки и соответствие стандартам.
2. **Tests:** Поднятие временных тестовых контейнеров (PostgreSQL + Redis) в облаке GitHub и запуск набора тестов (`manage.py test`).
3. **Deploy:** Выполняется строго при пуше или мердже в ветку `homework_35_2`/`main`. Скрипт безопасно подключается к продакшн-серверу через SSH, забирает свежий код, пересобирает контейнеры без остановки трафика и применяет новые миграции. На Pull Request деплой заблокирован.
