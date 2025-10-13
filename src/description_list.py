import pandas as pd
from collections import Counter

file_path = r"C:\Users\1\PycharmProjects\pythonProject\transactions_excel.xlsx"
transactions_df = pd.read_excel(file_path)
transactions_list = transactions_df.to_dict(orient='records')


def process_bank_operations(transactions: list[dict], categories: list) -> dict:
    """
    Функция принимает список словарей с данными о банковских операциях и список категорий операций,
    а возвращает словарь, в котором ключи — это названия категорий, а значения — это количество
    операций в каждой категории.
    """
    category_counts = Counter(
        operation.get('description') for operation in transactions if operation.get('description') in categories
    )
    return dict(category_counts)
