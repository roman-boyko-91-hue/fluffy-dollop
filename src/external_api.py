import os

import requests
from dotenv import load_dotenv

url = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"

payload = {}
headers = {
    "apikey": "{API-KEY}"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
result = response.text

load_dotenv()
API_KEY = os.getenv('API_KEY')

load_dotenv()
API_KEY = os.getenv('API_KEY')


def external_api(
        transaction):  # Реализауем функцию которая будет принимать транзакцию, а возвращать сумму после конвертации.

    from_currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    if from_currency == "RUB":
        return_amount = amount
        return return_amount

    elif from_currency in ("USD", "EUR"):

        to_currency = "RUB"
        url = (f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&"
               f"from={from_currency}&amount={amount}")
        payload = {}
        headers = {
            "apikey": API_KEY
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        status_code = response.status_code
        result = response.json()

        return result["result"] if status_code == 200 else f"Ошибка {status_code}"
