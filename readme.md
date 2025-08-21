# Приложение для банка

## Описание
Приложение для банка. Специальное такое _приложение_.
Она позволяет клиенту банка пользоваться банковскими _услугами_.

## Инструкции по установке

1. Скачайте любой __VPN__
2. Зайдите в __App Store__ или __Google Play__
3. Нажмите на кнопку __Скачать__
4. Подождите немного
5. __Наслаждайтесь__

## Что тут вообще есть
В приложении пока есть только несколько функций. 

### Модуль _mask_
- get_mask_card_number
_(Создает маску вашей кредитной карты)_
- get_mask_account
_(Создает маску вашего кредитного счета)_
### Модуль _widget_
- mask_account_card
_(Создает расширенную маску вашей кредитной карты)_
- get_date_(Просмотр даты)_
### Модуль _processing_
- filter_by_state
_(Просмотр ваших операций по статусу)_
- sort_by_date
_(Сортирует их по дате)_


## Примеры использования
- Функция ___get_mask_card_number___ принимает на вход номер карты 
и возвращает ее маску. Номер карты замаскирован и отображается 
в формате __XXXX XX** **** XXXX__, где __X__ — это цифра номера. 
То есть видны первые 6 цифр и последние 4 цифры, остальные 
символы отображаются звездочками, номер разбит по блокам 
по 4 цифры, разделенным пробелами. Пример работы функции:

     __7000792289606361__    _# входной аргумент_

     __7000 79** **** 6361__  _# выход функции_

- Функция ___get_mask_account___ принимает на вход номер счета 
и возвращает его маску. Номер счета замаскирован и отображается 
в формате __**XXXX__, где __X__ — это цифра номера. То есть видны 
только последние 4 цифры номера, а перед ними — две звездочки. Пример 
работы функции:

  __73654108430135874305__  _# входной аргумент_
  __**4305__  _# выход функции_


и т.д.

_to be continued_

_La fine_
    














Теперь давайте создадим файл для тестов. Назовем его `test_your_module.py` (предполагая, что ваш код находится в файле `your_module.py`).

```python
import pytest
from datetime import datetime
# Предполагается, что ваши функции находятся в файле 'your_module.py'
# Если они в другом файле, замените 'your_module' на соответствующее имя
from your_module import filter_by_state, sort_by_date

# --- Тесты для filter_by_state ---

def test_filter_by_state_default_executed():
    """Тест фильтрации по состоянию EXECUTED (по умолчанию)."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(data) == expected

def test_filter_by_state_custom_canceled():
    """Тест фильтрации по другому состоянию (CANCELED)."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    expected = [
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    assert filter_by_state(data, state="CANCELED") == expected

def test_filter_by_state_no_matches():
    """Тест, когда нет совпадений по состоянию."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    expected = []
    assert filter_by_state(data, state="PENDING") == expected

def test_filter_by_state_empty_list():
    """Тест с пустым входным списком."""
    data = []
    expected = []
    assert filter_by_state(data) == expected
    assert filter_by_state(data, state="CANCELED") == expected

def test_filter_by_state_item_not_in_dict():
    """Тест, когда ключ 'state' отсутствует в одном из словарей."""
    data = [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "status": "EXECUTED"}, # Здесь ключ 'state' отсутствует
        {"id": 3, "state": "CANCELED"},
    ]
    # Ваша функция `filter_by_state` ищет совпадение в ЛЮБОМ значении словаря.
    # Это может привести к неожиданному поведению, если в словаре есть другие ключи
    # со значением, совпадающим с `state`.
    # Если `state` присутствует, но другого ключа, который тоже совпадет, не будет,
    # то он будет правильно отфильтрован.
    # Здесь я предполагаю, что 'state' присутствует.
    expected_executed = [{"id": 1, "state": "EXECUTED"}]
    assert filter_by_state(data, state="EXECUTED") == expected_executed

    # Важное замечание: Ваша текущая реализация `filter_by_state`
    # имеет потенциальную проблему. Она будет добавлять `dict_item`,
    # если ЛЮБОЕ значение в словаре совпадет с `state`.
    # Например, если бы было `{"id": 5, "another_field": "EXECUTED"}`,
    # то этот словарь был бы добавлен при фильтрации по "EXECUTED",
    # даже если поле "state" там другое или отсутствует.
    # Более надежный подход:
    #
    # def filter_by_state_robust(list_not_filtered: list, state: str = "EXECUTED") -> list:
    #     list_filtered = []
    #     for dict_item in list_not_filtered:
    #         if dict_item.get("state") == state: # Используйте .get() для безопасности
    #             list_filtered.append(dict_item)
    #     return list_filtered
    #
    # Если вы измените функцию на более надежную, вам придется скорректировать этот тест.
    # Для текущей функции, если "another_field" = "EXECUTED", то:
    data_with_other_match = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 5, "another_field": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, # Это значение попадет в фильтр
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    ]
    expected_with_other_match = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 5, "another_field": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    assert filter_by_state(data_with_other_match) == expected_with_other_match


# --- Тесты для sort_by_date ---

def test_sort_by_date_descending_default():
    """Тест сортировки по дате по убыванию (по умолчанию)."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, # Самая поздняя
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, # Самая ранняя
    ]
    assert sort_by_date(data) == expected

def test_sort_by_date_ascending():
    """Тест сортировки по дате по возрастанию."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    expected = [
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}, # Самая ранняя
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}, # Самая поздняя
    ]
    assert sort_by_date(data, descending=False) == expected

def test_sort_by_date_empty_list():
    """Тест сортировки с пустым входным списком."""
    data = []
    expected = []
    assert sort_by_date(data) == expected
    assert sort_by_date(data, descending=False) == expected

def test_sort_by_date_single_item():
    """Тест сортировки списка с одним элементом."""
    data = [{"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]
    expected = [{"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]
    assert sort_by_date(data) == expected
    assert sort_by_date(data, descending=False) == expected

def test_sort_by_date_same_dates():
    """Тест сортировки, когда даты одинаковые. Порядок не должен меняться."""
    date_str = "2019-07-03T18:35:29.512364"
    data = [
        {"id": 1, "state": "EXECUTED", "date": date_str},
        {"id": 2, "state": "EXECUTED", "date": date_str},
        {"id": 3, "state": "CANCELED", "date": date_str},
    ]
    # Python `sorted` является стабильным, поэтому относительный порядок элементов
    # с одинаковыми ключами сортировки сохраняется.
    expected = [
        {"id": 1, "state": "EXECUTED", "date": date_str},
        {"id": 2, "state": "EXECUTED", "date": date_str},
        {"id": 3, "state": "CANCELED", "date": date_str},
    ]
    assert sort_by_date(data) == expected
    assert sort_by_date(data, descending=False) == expected

def test_sort_by_date_invalid_date_format():
    """Тест, когда формат даты некорректен."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "invalid-date"}, # Некорректный формат
    ]# Ожидаем, что `datetime.strptime` выбросит `ValueError`
    with pytest.raises(ValueError):
        sort_by_date(data)

def test_sort_by_date_missing_date_key():
    """Тест, когда ключ 'date' отсутствует в одном из словарей."""
    data = [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED"}, # Ключ 'date' отсутствует
    ]
    # Ожидаем, что `x[data_key]` (где data_key='date') выбросит `KeyError`
    with pytest.raises(KeyError):
        sort_by_date(data)

def test_sort_by_date_custom_key():
    """Тест сортировки по другому ключу (например, 'timestamp')."""
    data = [
        {"id": 1, "timestamp": "2019-07-03T18:35:29.512364"},
        {"id": 2, "timestamp": "2018-06-30T02:08:58.425572"},
    ]
    expected = [
        {"id": 2, "timestamp": "2018-06-30T02:08:58.425572"},
        {"id": 1, "timestamp": "2019-07-03T18:35:29.512364"},
    ]
    assert sort_by_date(data, data_key="timestamp", descending=False) == expected

### Как это использовать:

1.  **Сохраните ваш код:** Сохраните ваш код в файл, например, `your_module.py`.
2.  **Сохраните тесты:** Сохраните код тестов в файл с именем, начинающимся на `test_` (например, `test_your_module.py`), в том же каталоге, что и ваш основной файл.
3.  **Запустите `pytest`:** Откройте терминал или командную строку, перейдите в каталог, где находятся ваши файлы, и выполните команду:
    ```bash
    pytest
    


`pytest` автоматически обнаружит файл `test_your_module.py` и запустит все функции, имена которых начинаются с `test_`.

### Объяснение тестов:

**Для `filter_by_state`:**

*   **`test_filter_by_state_default_executed`**: Проверяет, что функция корректно фильтрует по состоянию "EXECUTED", когда `state` не указан (используется значение по умолчанию).
*   **`test_filter_by_state_custom_canceled`**: Проверяет фильтрацию по другому состоянию ("CANCELED") при явном указании параметра `state`.
*   **`test_filter_by_state_no_matches`**: Убеждается, что если нет ни одного словаря с указанным состоянием, возвращается пустой список.
*   **`test_filter_by_state_empty_list`**: Тестирует поведение функции при передаче пустого списка, ожидается пустой список.
*   **`test_filter_by_state_item_not_in_dict`**: **Важный тест!** Он проверяет, что происходит, если в словаре отсутствует ожидаемый ключ `state`. Ваша текущая реализация (`for item in dict_item.values(): if item == state:`) будет работать некорректно, если другие поля в словаре будут иметь значение, совпадающее с `state`. Я добавил комментарии и пример, показывающий эту потенциальную проблему. Если вы хотите более строгую фильтрацию только по ключу `state`, вам следует изменить вашу функцию.

**Для `sort_by_date`:**

*   **`test_sort_by_date_descending_default`**: Проверяет, что сортировка по умолчанию (по убыванию) работает правильно.
*   **`test_sort_by_date_ascending`**: Проверяет сортировку по возрастанию, когда `descending=False`.
*   **`test_sort_by_date_empty_list`**: Тестирует сортировку пустого списка.
*   **`test_sort_by_date_single_item`**: Проверяет, что список с одним элементом остается неизменным.
*   **`test_sort_by_date_same_dates`**: Убеждается, что при одинаковых датах порядок элементов сохраняется (стабильная сортировка).
*   **`test_sort_by_date_invalid_date_format`**: Использует `pytest.raises` для проверки того, что функция выбрасывает `ValueError`, если формат даты некорректен.
*   **`test_sort_by_date_missing_date_key`**: Использует `pytest.raises` для проверки, что функция выбрасывает `KeyError`, если ключ `date` отсутствует в одном из словарей.
*   **`test_sort_by_date_custom_key`**: Демонстрирует, как можно протестировать сортировку по другому ключу, если это потребуется.

Эти тесты покрывают основные сценарии использования ваших функций и помогут убедиться в их корректной работе.