from datetime import datetime

import pandas as pd
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
    last_of_month = date.replace(day=28)
    return [start_of_month, last_of_month]


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
    """Функция, которая принимает DataFrame и возвращает список карт с расходами и кэшбеком"""
    card_transaction = []
    for _, row in sorted_period.iterrows():
        card_data = {
            "last_digits": str(row["Номер карты"])[-4:],  # Последние 4 цифры
            "total_spent": row["Сумма операции с округлением"],
            "cashback": row["Кэшбэк"]
        }
        card_transaction.append(card_data)
    return card_transaction
