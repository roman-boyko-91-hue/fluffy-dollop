from unittest.mock import mock_open, patch

from src.transactions_csv import read_file_csv


@patch('builtins.open', new_callable=mock_open,
       read_data='id;state;date;amount;currency_name;currency_code;from;to;description\n'
                 '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;'
                 'Счет 39745660563456619397;Перевод организации')
def test_read_file_csv(mock_open):
    expected_result = [
        {
            'id': '650703', 'state': 'EXECUTED', 'date': '2023-09-05T11:30:32Z', 'amount': '16210',
            'currency_name': 'Sol', 'currency_code': 'PEN', 'from': 'Счет 58803664561298323391',
            'to': 'Счет 39745660563456619397', 'description': 'Перевод организации'
        }
    ]
    result = read_file_csv('dummy_path.csv')
    assert result == expected_result
