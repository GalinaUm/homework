from datetime import datetime
from pprint import pprint

from src.utils import read_transactions
from src.widget import get_date


def filter_by_state(list_not_filtered: list, state: str = "EXECUTED") -> list:
    """Функция, которая фильтрует списки словарей по нужному параметру"""

    if not list_not_filtered:
        raise ValueError("Пустой список")

    list_filtered = []
    for dict_item in list_not_filtered:
        for item in dict_item.values():
            if item == state:
                list_filtered.append(dict_item)
    return list_filtered


# state_2 = "CANCELED"


def sort_by_date(data: list[dict], is_reverse: bool = True) -> list[dict]:
    """
    Сортирует список словарей по значению ключа 'date'
    """
    sorted_by_date_data = sorted(
        data, key=lambda item: datetime.strptime(get_date(item["date"].split("T")[0]), "%d.%m.%Y"), reverse=is_reverse
    )
    return sorted_by_date_data


# Проверка работы кода
if __name__ == "__main__":
    pprint(
        sort_by_date(
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 111111111, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ]
        )
    )
