import os
import sys
from unittest import mock

from src.external_api import external_api

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from unittest.mock import patch

import requests


def get_api_info():
    response = requests.get(
        "https://api.apilayer.com/exchangerates_data/latest"
        "?apikey=2vvlfqblGXPqkfNvVm02M31gKTAk45O2&base=USD&symbols=RUB")
    return response.json()


@patch('requests.get')
def test_get_api_info(mock_get):
    mock_get.return_value.json.return_value = {"id": 41428829, "state": "EXECUTED"}
    assert get_api_info() == {"id": 41428829, "state": "EXECUTED"}
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/latest"
        "?apikey=2vvlfqblGXPqkfNvVm02M31gKTAk45O2&base=USD&symbols=RUB")


@mock.patch('requests.request')
def test_usd_success(mock_request):
    transaction = {
        "operationAmount": {
            "amount": "500",
            "currency": {
                "code": "EUR"
            }
        }
    }

    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 2000.0}
    mock_request.return_value = mock_response

    result = external_api(transaction)
    assert result == 2000.0

    mock_request.assert_called_once_with(
        "GET",
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=500",
        headers={"apikey": mock.ANY},
        data={}
    )


def test_rub_transaction():
    transaction = {
        "operationAmount": {
            "amount": "10000",
            "currency": {
                "code": "RUB"
            }
        }
    }

    result = external_api(transaction)
    assert result == "10000"
