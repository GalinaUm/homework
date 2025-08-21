from datetime import datetime


def filter_by_state(list_not_filtered: list, state: str = "EXECUTED") -> list:
    """Функция, которая фильтрует списки словарей по нужному параметру"""
    list_filtered = []
    for dict_item in list_not_filtered:
        for item in dict_item.values():
            if item == state:
                list_filtered.append(dict_item)
    return list_filtered


state_2 = "CANCELED"
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)


def sort_by_date(data_list: list, data_key: str = "date", descending=True) -> list:
    """Функция, которая принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание). Функция должна возвращать
     новый список, отсортированный по дате(date)."""
    return sorted(data_list, key=lambda x: datetime.strptime(x[data_key], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending)


# Проверка работы кода
if __name__ == "__main__":
    print(
        sort_by_date(
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ]
        )
    )

