import re

file_path = r"C:\Users\1\PycharmProjects\pythonProject\transactions_excel.xlsx"


def search_transactions(transactions: list[dict], search: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и
    строку поиска, а возвращает список словарей, в описании кт есть данная строка.
    """
    results = []
    for transaction in transactions:
        if re.search(search, description, flags=re.IGNORECASE) and isinstance(transaction['description'], str):
            if search in transaction['description']:
                results.append(transaction)
    return results


print(search_transactions(transactions, search))
