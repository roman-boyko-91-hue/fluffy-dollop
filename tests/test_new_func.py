from unittest.mock import mock_open, patch

from main.main import main
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


def test_main():
    """Тестирование функции, в которой подставляются данные вместо реального содержимого файла"""
    mock_data = '[{"id": 4419458862}]'

    # Используем patch для замены функции open на mock_open
    with patch('builtins.open', mock_open(read_data=mock_data)):
        transactions = main('path\to\mock_file.json')

        # Проверяем, что данные из mock_data были считаны и обработаны правильно
        assert transactions == [{"id": 4419458862}]
