from datetime import datetime

from pandas import DataFrame


def get_greetings(date: datetime) -> str:
    """Функция выдает "приветствие" в зависимости от текущего времени"""
    hour = date.hour
    if 6 <= hour < 12:
        return "Доброе утро"
    elif 12 <= hour < 17:
        return "Добрый день"
    elif 18 <= hour < 23:
        return "Добрый вечер"
    else:
        return "Доброй ночи"


def get_period_of_date(date: str) -> list[str]:
    start_of_month = date.replace(day=1)


def get_sorted_period(path_to_file: str, date_period: list) -> DataFrame:
