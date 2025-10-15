import re

import pandas as pd

file_path = r"C:\Users\1\PycharmProjects\pythonProject\transactions_excel.xlsx"
transactions_df = pd.read_excel(file_path)
transactions_list = transactions_df.to_dict(orient='records')


def search_transactions(transactions: list[dict], search: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и
    строку поиска, а возвращает список словарей, в описании кт есть данная строка.
    """
    results = []
    for transaction in transactions:
        if isinstance(transaction['description'], (str, float)):
            description = str(transaction['description'])
            if re.search(search, description, flags=re.IGNORECASE):
                results.append(transaction)

    return results


print(search_transactions(transactions_list, 'перевод'))
