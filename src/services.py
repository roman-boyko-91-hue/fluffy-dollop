import json

import pandas as pd
from typing import List, Dict


def cashback_analyze(transactions: List[Dict], year: int, month: int) -> dict:
    """Функция, которая анализирует выгодные категории кэшбэка"""
    df = pd.DataFrame(transactions)
    df["Дата операции"] = pd.to_datetime(df["Дата операции"], format="%d.%m.%Y %H:%M:%S")
    filter_data = df[(df["Дата операции"].dt.year == year) &
                     (df["Дата операции"].dt.month == month) &
                     (df["Кэшбэк"] > 0)]
    expenses_by_category = filter_data.groupby("Категория")["Сумма платежа"].sum()
    cashback_by_category = abs(expenses_by_category) // 100

    result = cashback_by_category.to_dict()
    return json.dumps(result, ensure_ascii=False, indent=4)
