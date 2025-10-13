import re


def search_transactions(transactions: list[dict], search: str) -> list[dict]:
    """
    Функция принимает список словарей с данными о банковских операциях и
    строку поиска, а возвращает список словарей, в описании кт есть данная строка.
    """
    results = re.findall(r"[dict]")
    for transaction in transactions:
        if 'description' in transaction and isinstance(transaction['description'], str):
            if search in transaction['description']:
                results.append(transaction)
    return results

print(search_transactions(transactions, search))
