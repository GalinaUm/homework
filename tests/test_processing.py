import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.fixture()
def data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]),
])
def test_filter_by_state(data, state, expected):
    assert filter_by_state(data, state) == expected


@pytest.mark.parametrize("state, expected", [
    ("CANCELED", [
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]),
])
def test_filter_by_state_custom_canceled(data, state, expected):
    """Тест фильтрации по другому состоянию (CANCELED)."""
    assert filter_by_state(data, state) == expected


def test_filter_by_state_no_data():
    with pytest.raises(ValueError):
        filter_by_state([])


def test_sort_by_date_ascending_and_descending():
    """1. Тестирование сортировки списка словарей по датам в порядке убывания и возрастания."""

    data = [
        {"id": 1, "date": "2023-10-26T10:00:00.000000"},
        {"id": 2, "date": "2023-10-25T12:00:00.000000"},
        {"id": 3, "date": "2023-10-27T08:00:00.000000"},
    ]

    # Тест на сортировку по убыванию (descending=True - по умолчанию)
    sorted_desc = sort_by_date(data)
    assert sorted_desc[0]["date"] == "2023-10-27T08:00:00.000000"
    assert sorted_desc[1]["date"] == "2023-10-26T10:00:00.000000"
    assert sorted_desc[2]["date"] == "2023-10-25T12:00:00.000000"

    # Тест на сортировку по возрастанию (descending=False)
    sorted_asc = sort_by_date(data, descending=False)
    assert sorted_asc[0]["date"] == "2023-10-25T12:00:00.000000"
    assert sorted_asc[1]["date"] == "2023-10-26T10:00:00.000000"
    assert sorted_asc[2]["date"] == "2023-10-27T08:00:00.000000"


def test_sort_by_date_with_equal_dates():
    """
    2. Проверка корректности сортировки при одинаковых датах.
    (Порядок элементов с одинаковыми датами не гарантируется stable sort,
     но проверяем, что они группируются и нет ошибок)
    """
    data = [
        {"id": 1, "date": "2023-10-26T10:00:00.000000"},
        {"id": 2, "date": "2023-10-25T12:00:00.000000"},
        {"id": 3, "date": "2023-10-26T10:00:00.000000"}, # Такая же дата
        {"id": 4, "date": "2023-10-27T08:00:00.000000"},
        {"id": 5, "date": "2023-10-25T12:00:00.000000"}, # Такая же дата
    ]

    sorted_desc = sort_by_date(data)

    # Проверяем, что элементы с одинаковыми датами стоят рядом
    # и общий порядок убывания соблюдается.
    # Для одинаковых дат порядок может быть разным, но эти элементы должны быть
    # последовательно в отсортированном списке.
    assert sorted_desc[0]["date"] == "2023-10-27T08:00:00.000000"

    # Проверяем группу с датой 2023-10-26
    assert sorted_desc[1]["date"] == "2023-10-26T10:00:00.000000"
    assert sorted_desc[2]["date"] == "2023-10-26T10:00:00.000000"

    # Проверяем группу с датой 2023-10-25
    assert sorted_desc[3]["date"] == "2023-10-25T12:00:00.000000"
    assert sorted_desc[4]["date"] == "2023-10-25T12:00:00.000000"


def test_sort_by_date_with_invalid_date_formats():
    # Случай с некорректным форматом даты
    invalid_format_data = [
        {"id": 1, "date": "2023-10-26T10:00:00.000000"},
        {"id": 2, "date": "26/10/2023 10:00"}, # Некорректный формат
        {"id": 3, "date": "2023-10-27T08:00:00.000000"},
    ]
    with pytest.raises(ValueError, match="time data '26/10/2023 10:00' does not match format '%Y-%m-%dT%H:%M:%S.%f'"):
        sort_by_date(invalid_format_data)

    # Случай с отсутствующим ключом "date"
    missing_key_data = [
        {"id": 1, "date": "2023-10-26T10:00:00.000000"},
        {"id": 2, "timestamp": "2023-10-25T12:00:00.000000"}, # Отсутствует 'date'
        {"id": 3, "date": "2023-10-27T08:00:00.000000"},
    ]
    with pytest.raises(KeyError, match="date"): # Или другой код ошибки, если `x[data_key]` вызовет ее
        sort_by_date(missing_key_data)

    # Случай с датой, которая не может быть преобразована (например, неполная)
    incomplete_date_data = [
        {"id": 1, "date": "2023-10-26T10:00:00.000000"},
        {"id": 2, "date": "2023-10-25T12:00:00"}, # Отсутствуют микросекунды
        {"id": 3, "date": "2023-10-27T08:00:00.000000"},
    ]
    with pytest.raises(ValueError, match="time data '2023-10-25T12:00:00' does not match format '%Y-%m-%dT%H:%M:%S.%f'"):
        sort_by_date(incomplete_date_data)

    # Случай с пустым списком
    empty_list_data = []
    sorted_empty = sort_by_date(empty_list_data)
    assert sorted_empty == []