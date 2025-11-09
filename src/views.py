import json
from datetime import datetime
from typing import Dict, Any


from utils import get_greetings, get_period_of_date, get_sorted_period, get_card_info, get_top_transactions, \
    get_currency, get_stock_prices


def main(date: str) -> Dict[str, Any]:
    """Главная функция, принимающая на вход строку с датой и временем в формате
YYYY-MM-DD HH:MM:SS и возвращающая JSON-ответ с некими данными"""
    date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    date_str = date.strftime("%Y-%m-%d %H:%M:%S")
    result = {}
    period_of_date = get_period_of_date(date)
    sorted_period = get_sorted_period("../data/operations.xlsx", period_of_date)
    # Приветствие
    greetings = get_greetings(date)

    # По каждой карте
    card_info = get_card_info(sorted_period)

    # Топ-5 транзакций по сумме платежа
    top_transactions = get_top_transactions(sorted_period, 5)

    # Курсы валют
    currency_rates = get_currency("../data/user_settings.json")

    # Стоимость акций
    stock_prices = get_stock_prices("../data/user_settings.json")

    json_result = json.dumps({"date": date_str, "greetings": greetings, "card_info": card_info}, ensure_ascii=False,
                             indent=4)
    #print(json_result)
    result = {
        "date": date_str,
        "greetings": greetings,
        "card_info": card_info,
        "top_transactions": top_transactions,
        "currency_rates": currency_rates,
        "stock_prices": stock_prices
    }

    return result
