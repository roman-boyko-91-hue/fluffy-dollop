import json
import calendar
from datetime import datetime

import pandas as pd
from pandas import DataFrame
from api import external_api


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
    """Возвращает [начало_месяца, конец_месяца] для переданной даты."""
    start_of_month = date.replace(day=1, hour=0, minute=0, second=0)
    last_day = calendar.monthrange(date.year, date.month)[1]
    end_of_month = date.replace(day=last_day, hour=23, minute=59, second=59)
    return [start_of_month, end_of_month]


def get_sorted_period(path_to_file: str, period_date: list) -> DataFrame:
    """Функция, которая принимает путь к эксель-файлу и периоду, а возвращает данные в этом периоде"""
    df = pd.read_excel(path_to_file, sheet_name="Отчет по операциям")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    start_of_date = period_date[0].strftime("%Y-%m-%d %H:%M:%S")
    last_of_date = period_date[1].strftime("%Y-%m-%d %H:%M:%S")

    filter_df = df[(df['Дата операции'] >= start_of_date) & (df['Дата операции'] <= last_of_date)]
    sorted_period = filter_df.sort_values(by="Дата операции", ascending=True)
    return sorted_period


def get_card_info(sorted_period: DataFrame) -> list[dict]:
    """Функция, которая принимает DataFrame и возвращает список карт с расходами и кэшбэком"""
    card_transaction = []
    for i, row in sorted_period.iterrows():
        card_data = {
            "last_digits": str(row["Номер карты"])[-4:],  # Последние 4 цифры
            "total_spent": row["Сумма операции с округлением"],
            "cashback": row["Кэшбэк"]
        }
        card_transaction.append(card_data)
    return card_transaction


def get_top_transactions(sorted_period: DataFrame, get_top):
    """Функция возвращает топ-5 транзакций по сумме платежа"""
    top_pay_transaction = []
    sorted_pay = sorted_period.sort_values(by="Сумма операции", ascending=True)
    top_transactions = sorted_pay.head(get_top)
    top_transaction_sorted = top_transactions[
        [
            "Дата платежа",
            "Сумма операции",
            "Категория",
            "Описание"
        ]
    ]

    for i, row in top_transaction_sorted.iterrows():
        item = {
            "date": f'{row["Дата платежа"]}',
            "amount": f'{row["Сумма операции"]}',
            "category": f'{row["Категория"]}',
            "description": f'{row["Описание"]}',
        }
        top_pay_transaction.append(item)

    return top_pay_transaction


def get_currency(path_to_json: str) -> list[dict]:
    """Функция, которая принимает на вход json-файл и возвращает курс валют"""
    currency_rates = []
    with open(path_to_json, "r", encoding="utf-8") as file:
        data = json.load(file)
        currencies = data["user_currencies"]
        for currency in currencies:
            amount = 1
            converted_amount = external_api(currency, amount)
            currency_rates.append({"currency": currency, "converted_amount": converted_amount})
    return currency_rates


def get_stock_prices(path_to_json: str) -> list[dict]:
    """Функция, которая принимает на вход json-файл и возвращает стоимость акций"""
    stock_rates = []
    with open(path_to_json, "r", encoding="utf-8") as file:
        data = json.load(file)
        stocks = data["user_stocks"]
        for stock in stocks:
            currency = stock
            amount = 1
            converted_amount = external_api(currency, amount)
            stock_rates.append({"currency": currency, "converted_amount": converted_amount})
        return stock_rates
