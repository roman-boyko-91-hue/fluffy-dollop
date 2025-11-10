import unittest
from services import cashback_analyze


class TestCashbackAnalyze(unittest.TestCase):
    def test_cashback_analyze_basic(self):
        # Пример транзакций
        transactions = [
            {"Дата операции": "10.01.2023 12:34:56", "Кэшбэк": 10, "Сумма платежа": 100, "Категория": "Продукты"},
            {"Дата операции": "11.01.2023 13:34:56", "Кэшбэк": 5, "Сумма платежа": 200, "Категория": "Одежда"},
            {"Дата операции": "12.01.2023 14:34:56", "Кэшбэк": 0, "Сумма платежа": 300, "Категория": "Электроника"}
        ]
        expected_result = '{\n    "Продукты": 1,\n    "Одежда": 2\n}'
        self.assertEqual(cashback_analyze(transactions, 2023, 1), expected_result)

    def test_cashback_analyze_no_cashback(self):
        transactions = [
            {"Дата операции": "10.01.2023 12:34:56", "Кэшбэк": 0, "Сумма платежа": 100, "Категория": "Продукты"}
        ]
        expected_result = '{}'
        self.assertEqual(cashback_analyze(transactions, 2023, 1), expected_result)


if __name__ == '__main__':
    unittest.main()
