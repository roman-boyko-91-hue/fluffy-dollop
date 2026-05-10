import requests
from celery_1 import shared_task
from django.conf import settings
from habits.models import Habit
from datetime import datetime


@shared_task
def send_habit_reminder():
    """Задача для рассылки напоминаний о привычках в Telegram"""

    # Фильтруем привычки: берем только те, время которых совпадает с текущим
    # Сравниваем часы и минуты
    now = datetime.now().time()
    habits = Habit.objects.filter(time__hour=now.hour, time__minute=now.minute)

    token = settings.TELEGRAM_TOKEN
    url = f"https://telegram.org{token}/sendMessage"

    for habit in habits:
        chat_id = habit.user.tg_chat_id

        if chat_id:
            message = f"Напоминание! Пора {habit.action} в {habit.place}."

            try:
                response = requests.post(
                    url,
                    data={
                        "chat_id": chat_id,
                        "text": message
                    },
                    timeout=10
                )
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Ошибка отправки для {habit.user.email}: {e}")
