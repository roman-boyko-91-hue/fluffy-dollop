import os
import sys

import pytest

from saver.py import JSONSaver

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


@pytest.fixture
def setup_saver(tmp_path):
    """Создаём временный путь для хранения файла"""
    temp_file = tmp_path / "test_vacancies.json"
    saver = JSONSaver(file_name=str(temp_file))
    return saver
