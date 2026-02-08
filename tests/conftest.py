import os
import sys

import pytest

from src.saver import JSONSaver

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def setup_saver(tmp_path):
    """Передаем путь к файлу"""
    temp_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'vacancies.json')
    saver = JSONSaver(file_path=temp_file)
    return saver
