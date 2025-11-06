import json
from datetime import datetime
from typing import Dict, Any

from mypy.util import json_dumps

from utils import get_greetings, get_period_of_date, get_sorted_period


def main(date: str) -> Dict[str, Any]:
    """Главная функция, принимающая на вход строку с датой и временем в формате
YYYY-MM-DD HH:MM:SS и возвращающая JSON-ответ с некими данными"""
    old_format_date = "12.04.2023"
    parsed_date = datetime.strptime(old_format_date, "%d.%m.%Y")
    new_format_date = parsed_date.strftime("%Y-%m-%d")
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    result = {}
    greetings = get_greetings(date)
    period_of_date = get_period_of_date(date)
    sorted_period = get_sorted_period("../data/operations.xlsx", period_of_date)
    result["greetings"] = greetings
    json_date = json_dumps(date, ensure_ascii=False, indent=4)

    return result
