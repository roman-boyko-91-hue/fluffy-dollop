import json
from datetime import datetime
from typing import Dict, Any

from mypy.util import json_dumps

from utils import get_greetings, get_period_of_date, get_sorted_period, get_card_info


def main(date: str) -> Dict[str, Any]:
    """Главная функция, принимающая на вход строку с датой и временем в формате
YYYY-MM-DD HH:MM:SS и возвращающая JSON-ответ с некими данными"""
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    result = {}
    greetings = get_greetings(date)
    period_of_date = get_period_of_date(date)
    sorted_period = get_sorted_period("../data/operations.xlsx", period_of_date)
    card_info = get_card_info(sorted_period)
    json_result = json.dumps({"date": date_str, "greetings": greetings, "card_info": card_info}, ensure_ascii=False,
                             indent=4)
    print(json_result)
    result = {
        "date": date_str,
        "greetings": greetings,
        "card_info": card_info
    }

    return result
