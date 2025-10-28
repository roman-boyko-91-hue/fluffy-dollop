from typing import Any, Dict, Iterator, List

transaction = [{"id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount":
                    {"amount": "9824.07",
                     "currency": {
                         "name": "USD",
                         "code": "USD"}
                     },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"},
               {"id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"}
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"}]


def filter_by_currency(transaction: List[Dict[Any, Any]], currency: str) -> Iterator[Dict[Any, Any]]:
    """Функция, которая принимает на вход список словарей, представляющих транзакции и валюту для фильтрации"""
    filtered_currency = list(
    filter(lambda x: 'operationAmount' in x and 'currency' in x['operationAmount'] or x['currency_code'] == currency, transaction)
)
    for trans in filtered_currency:
        yield trans


def transaction_descriptions(transaction: list) -> Iterator[str]:
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди."""
    for trans in transaction:
        yield trans["description"]


descriptions = transaction_descriptions(transaction)
try:
    for _ in range(5):
        (next(descriptions))
except StopIteration:
    "Больше нет транзакций."


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """Генератор, который генерирует номера банковских карт в заданном диапазоне."""
    for number in range(start, end + 1):
        card_number = f"{number:016d}"
        format_card_number = " ".join([card_number[i:i + 4] for i in range(0, 16, 4)])
        yield format_card_number
