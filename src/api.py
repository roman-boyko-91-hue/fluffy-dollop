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


def external_api(from_currency, amount):
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


load_dotenv()
API_KEY = os.getenv('API_KEY')
