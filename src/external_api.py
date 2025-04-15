import os
import requests
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(transaction: Dict[str, Any]) -> float:
    """
    Конвертирует сумму транзакции в рубли. Если валюта USD или EUR, запрашивает курс через API.

    Args:
        transaction (Dict[str, Any]): Словарь с данными о транзакции.

    Returns:
        float: Сумма транзакции в рублях.
    """
    amount = transaction.get('amount', 0.0)
    currency = transaction.get('currency', 'RUB')

    if currency == 'RUB':
        return float(amount)

    if currency in ['USD', 'EUR']:
        api_key = os.getenv('EXCHANGE_API_KEY')
        url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
        headers = {"apikey": api_key}

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            rate = response.json()['rates']['RUB']
            return float(amount * rate)
        except (requests.RequestException, KeyError):
            return 0.0

    return 0.0
