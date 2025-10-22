import csv
from typing import Any

file_name = r"C:\Users\1\PycharmProjects\pythonProject\transactions.csv"


def read_file_csv(file_name: str) -> list[Any] | None:
    """Функция для считывания финансовых операций. Принимает на вход файл.csv,
    возвращает список словарей
    """

    try:
        with open(file_name, mode='r', encoding='utf-8') as file_csv:
            reader = csv.DictReader(file_csv, delimiter=';')
            result_dict = []
            for row in reader:
                result_dict.append(row)
            return result_dict
    except Exception as e:
        return f"Ошибка {e}"


print(read_file_csv(file_name))
