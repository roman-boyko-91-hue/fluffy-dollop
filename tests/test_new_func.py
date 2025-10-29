from src.description import search_transactions
from src.description_list import process_bank_operations


def test_search_transactions(transactions):
    """Тестирование строки поиска"""
    search = "Маркет"
    result = []
    assert search_transactions(transactions, search) == result


def test_process_bank_operations():
    """Тестирование ожидаемого результата"""
    transactions = [
        {'description': 'Перевод', 'amount': 100},
        {'description': 'Оплата', 'amount': 200},
    ]
    categories = ['Перевод', 'Оплата']
    expected_result = {'Перевод': 1, 'Оплата': 1}

    result = process_bank_operations(transactions, categories)
    assert result == expected_result
