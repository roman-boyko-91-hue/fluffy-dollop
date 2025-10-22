import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.decorators import log


@log(filename=None)
def func(x, y):
    return x + y


def test_func():
    """Тестирование с ожидаемым результатом"""
    result = func(3, 8)
    assert result == 11


def test_func_caps(capsys):
    """Тестирование декоратора с помощью фикстутры 'capsys'"""
    result = func(3, 8)
    captured = capsys.readouterr()
    output = captured.out
    assert "Результат: 11" in output
