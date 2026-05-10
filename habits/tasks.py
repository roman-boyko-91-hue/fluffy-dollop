import requests
from celery import shared_task
from django.conf import settings
from habits.models import Habit


@shared_task
def send_habit_reminder():
    """Задача для рассылки напоминаний о привычках в Telegram"""

    # Получаем все привычки
    habits = Habit.objects.all()
    token = settings.TELEGRAM_TOKEN
    url = f"https://telegram.org{token}/sendMessage"

    for habit in habits:
        # Проверяем, есть ли у владельца привычки chat_id
        chat_id = habit.user.tg_chat_id

        if chat_id:
            message = f"Напоминание! Время для привычки: {habit.action} в {habit.place}. Время: {habit.time}"

            try:
                response = requests.post(
                    url,
                    data={
                        "chat_id": chat_id,
                        "text": message
                    },
                    timeout=10  # Чтобы задача не висела при плохой сети
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Ошибка отправки для {habit.user.email}: {e}")
