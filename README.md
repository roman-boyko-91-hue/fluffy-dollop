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

## Непрерывная интеграция и развертывание (CI/CD)

В проекте настроен автоматический пайплайн сборки, тестирования и деплоя на базе **GitHub Actions**. Каждое изменение в коде проходит строгую проверку перед тем, как попасть на сервер.

### Схема работы пайплайна

Пайплайн разделен на три последовательные стадии (Jobs):

1. **Lint (Проверка стиля кода)**
   * Запускается при каждом `push` и `pull_request` в ветку `main`.
   * Использует линтеры (`flake8` / `black` / `ruff`) для проверки соответствия кода стандарту PEP 8.
   * Если код оформлен неверно, сборка падает.

2. **Tests (Тестирование)**
   * Стартует автоматически после успешного прохождения стадии линтинга.
   * Разворачивает тестовое окружение на Python 3.13.
   * Запускает юнит-тесты и интеграционные тесты (`pytest`).
   * Гарантирует, что новые изменения не ломают существующий функционал.

3. **Deploy (Развертывание)**
   * Запускается **только** при слиянии (merge) PR в ветку `main` и условии, что тесты и линтер прошли успешно.
   * Подключается к виртуальной машине в **Yandex Cloud** по протоколу SSH.
   * Выполняет команды обновления репозитория на сервере:
     ```bash
     git pull origin main
     docker compose down
     docker compose up --build -d
     ```
   * Благодаря политике `restart: always` в `docker-compose.yaml`, контейнеры (Nginx, Gunicorn/Python 3.13) автоматически перезапускаются и подтягивают новые изменения без долгого простоя (Downtime).

### Настройка секретов (GitHub Secrets)

Для безопасности все конфиденциальные данные скрыты. Чтобы деплой работал, в настройках репозитория (`Settings -> Secrets and variables -> Actions`) должны быть заданы следующие переменные:
* `SSH_KEY` — приватный SSH-ключ для доступа к ВМ в Yandex Cloud.
* `SERVER_IP` — публичный IP-адрес виртуальной машины.
* `SERVER_USER` — имя пользователя на сервере.
