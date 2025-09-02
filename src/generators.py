from typing import Dict, Iterator, List

def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[Dict]:
    """Функция, которая возвращает итератор, выдающий транзакции, где валюта операции соответствует заданной"""

    result = (
        transaction
        for transaction in transactions
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )

    return result


def transaction_descriptions(transactions: list[dict]) -> Iterator:
    """Генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""

    for transaction in transactions:
        description = transaction.get("description")
        yield description