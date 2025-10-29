import json
import logging
import os
from typing import Any, Dict, List

# Реализация записей логов в файл
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_transactions_from_json(file_path: str) -> List[Dict[str, Any]]:
    """
    Реализуйте функцию, которая принимает на вход путь до JSON-файла и возвращает
    список словарей с данными о финансовых транзакциях. Если файл пустой,
    содержит не список или не найден, функция возвращает пустой список.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            transactions = json.load(f)

            if isinstance(transactions, list):
                logger.info("Файл с данными существует")
                return transactions

            return transactions
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {file_path}")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: Файл '{file_path}' пустой.")
        return []


result = get_transactions_from_json(os.path.join(os.path.dirname(os.path.dirname(__file__)),
                                                 "data", "operations.json"))
