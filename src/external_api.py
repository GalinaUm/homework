import os

import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_KEY")


def convert(transaction: dict) -> float:
    """Возвращает сумму, если она в рублях, и сначала конвертирует, если в другой валюте"""
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if currency == "RUB":
        return amount

    url = "https://api.apilayer.com/exchangerates_data/convert"
    headers = {"apikey": API_KEY}
    params = {"from": currency, "to": "RUB", "amount": amount}

    response = requests.get(url, headers=headers, params=params)
    return response.json()["result"]


if __name__ == "__main__":
    print(
        convert(
            {
                "date": "2019-08-16T04:23:41.621065",
                "description": "Перевод с карты на счет",
                "from": "MasterCard 8826230888662405",
                "id": 86608620,
                "operationAmount": {"amount": "6004.00", "currency": {"code": "USD", "name": "руб."}},
                "state": "EXECUTED",
                "to": "Счет 96119739109420349721",
            }
        )
    )
