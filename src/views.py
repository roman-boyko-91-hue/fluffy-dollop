from datetime import datetime

from utils import get_greetings


def main(date: str) -> dict:
    """Главная функция, принимающую на вход строку с датой и временем в формате
YYYY-MM-DD HH:MM:SS и возвращающая JSON-ответ с некими данными"""
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    result = {}
    greetings = get_greetings(date)
    result["greetings"] = greetings
    card_info =
    pass
    return result

print(main("2025-11-05 00:00:00"))
