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


def get_sorted_period(path_to_file: str, period_date: list) -> DataFrame:
    """Функция, которая принимает путь к эксель-файлу и период, а возвращает данные в этом периоде"""
    df = pd.read_excel(path_to_file, sheet_name="Отчет по операциям")
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], dayfirst=True)
    start_of_date = datetime.strptime(period_date[0])
    last_of_date = datetime.strptime(period_date[1])

    filter_df = df[start_of_date <= df["Дата операции"] <= last_of_date]
    print(filter_df)
