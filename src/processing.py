from datetime import datetime
from pprint import pprint

from src.utils import read_transactions


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




def sort_by_date(data_list: list, data_key: str = "date", descending=True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
     новый список, отсортированный по дате(date)."""
    return sorted(data_list, key=lambda x: datetime.strptime(x[data_key], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending)


# Проверка работы кода
if __name__ == "__main__":
    pprint(filter_by_state(read_transactions('../data/operations.json')))

