import os
import sys

# Добавляем корневую директорию проекта в PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import pytest


@pytest.fixture
def transactions():
    return [
        {
            "description": "Перевод организации",
            "amount": 16210
        },
        {
            "description": "Перевод с карты на карту",
            "amount": 29740
        },
        {
            "description": "Открытие вклада",
            "amount": 23789
        }
    ]

@pytest.fixture
def search():
    return [
        {
            "description": "Перевод организации",
            "amount": 16210
        },
        {
            "description": "Перевод с карты на карту",
            "amount": 29740
        },
        {
            "description": "Открытие вклада",
            "amount": 23789
        }
    ]
