from datetime import datetime


def get_greetings(date: datetime) -> str:
    hour = date.hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"