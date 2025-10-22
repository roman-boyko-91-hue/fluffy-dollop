import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import mock_open, patch

from src.utils import get_transactions_from_json


def test_load_transactions():
    """Тестирование функции, в которой подставляются данные вместо реального содержимого файла"""
    mock_data = '[{"id": 4419458862}]'

    # Используем patch для замены функции open на mock_open
    with patch('builtins.open', mock_open(read_data=mock_data)):
        transactions = get_transactions_from_json('path/to/mock_file.json')

        # Проверяем, что данные из mock_data были считаны и обработаны правильно
        assert transactions == [{"id": 4419458862}]
