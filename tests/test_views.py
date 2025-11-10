import unittest
from unittest.mock import patch
from src import main


class TestMainFunction(unittest.TestCase):
    @patch('utils.get_greetings', return_value='Добрый день!')
    @patch('utils.get_period_of_date', return_value='some_period')
    @patch('utils.get_sorted_period', return_value=[{'data': 'test'}])
    @patch('yutils.get_card_info', return_value={'info': 'card_info'})
    @patch('utils.get_top_transactions', return_value=['top1', 'top2'])
    @patch('utils.get_currency', return_value={'USD': 74.0})
    @patch('utils.get_stock_prices', return_value={'AAPL': 150.0})
    def test_main_basic(self, mock_get_greetings, mock_get_period_of_date, mock_get_sorted_period,
                        mock_get_card_info, mock_get_top_transactions, mock_get_currency, mock_get_stock_prices):
        expected_result = {
            "date": "2023-01-10 12:34:56",
            "greetings": "Добрый день!",
            "card_info": {'info': 'card_info'},
            "top_transactions": ['top1', 'top2'],
            "currency_rates": {'USD': 74.0},
            "stock_prices": {'AAPL': 150.0}
        }
        self.assertEqual(main("2023-01-10 12:34:56"), expected_result)


if __name__ == '__main__':
    unittest.main()
