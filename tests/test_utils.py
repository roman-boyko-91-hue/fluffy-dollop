import unittest
from unittest.mock import patch
from datetime import datetime
from utils import get_greetings
from utils import get_period_of_date
from utils import get_currency, get_stock_prices


class TestGetGreetings(unittest.TestCase):
    def test_morning(self):
        date = datetime(2023, 1, 1, 8, 0, 0)  # 8:00 AM
        self.assertEqual(get_greetings(date), "Доброе утро")

    def test_afternoon(self):
        date = datetime(2023, 1, 1, 13, 0, 0)  # 1:00 PM
        self.assertEqual(get_greetings(date), "Добрый день")

    def test_evening(self):
        date = datetime(2023, 1, 1, 19, 0, 0)  # 7:00 PM
        self.assertEqual(get_greetings(date), "Добрый вечер")

    def test_night(self):
        date = datetime(2023, 1, 1, 3, 0, 0)  # 3:00 AM
        self.assertEqual(get_greetings(date), "Доброй ночи")


class TestGetPeriodOfDate(unittest.TestCase):
    def test_period(self):
        date = datetime(2023, 1, 15)
        period = get_period_of_date(date)
        self.assertEqual(period[0], datetime(2023, 1, 1, 0, 0, 0))  # Start of the month
        self.assertEqual(period[1], datetime(2023, 1, 31, 23, 59, 59))  # End of the month

    class TestExternalAPIs(unittest.TestCase):
        @patch('your_module.external_api', return_value=100.0)
        def test_get_currency(self, mock_external_api):
            result = get_currency('path_to_user_settings.json')
            self.assertEqual(len(result), 2)  # Предположим, что в JSON два курса
            self.assertEqual(result[0]['converted_amount'], 100.0)

        @patch('your_module.external_api', return_value=150.0)
        def test_get_stock_prices(self, mock_external_api):
            result = get_stock_prices('path_to_user_settings.json')
            self.assertEqual(len(result), 2)  # Предположим, что в JSON две акции
            self.assertEqual(result[0]['converted_amount'], 150.0)

    if __name__ == '__main__':
        unittest.main()
