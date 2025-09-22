import json
import unittest
from collections import Counter
from unittest.mock import mock_open, patch, Mock

from src.utils import read_transactions, process_bank_search, process_bank_operations


class TestReadTransactions(unittest.TestCase):
    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", new_callable=mock_open)
    def test_read_transactions_success(self, mock_file_open, mock_os_exists):
        file_path = "../data/operations.json"
        expected_data = [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            }
        ]
        # Настраиваем поведение заглушек
        mock_os_exists.return_value = True  # Файл существует
        mock_file_open.return_value.read.return_value = json.dumps(expected_data)  # Содержимое файла

        # Вызываем тестируемую функцию
        result = read_transactions(file_path)

        # Проверяем результат
        self.assertEqual(result, expected_data)

        # Проверяем, что os.path.exists был вызван с правильным путем
        mock_os_exists.assert_called_once_with(file_path)

        # Проверяем, что open был вызван с правильными аргументами
        mock_file_open.assert_called_once_with(file_path, "r", encoding="utf-8")

        # Проверяем, что read был вызван
        mock_file_open.return_value.read.assert_called_once()

    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", new_callable=mock_open)
    def test_read_transactions_empty_json_list(self, mock_file_open, mock_os_exists):
        """
        Тестирует чтение файла, который содержит пустой JSON-список.
        """
        file_path = "../data/operations.json"
        empty_list_data = []

        mock_os_exists.return_value = True
        mock_file_open.return_value.read.return_value = json.dumps(empty_list_data)

        result = read_transactions(file_path)

        self.assertEqual(result, empty_list_data)
        mock_os_exists.assert_called_once_with(file_path)
        mock_file_open.assert_called_once_with(file_path, "r", encoding="utf-8")

    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", new_callable=mock_open)
    def test_read_transactions_not_a_list(self, mock_file_open, mock_os_exists):
        """
        Тестирует чтение файла, который содержит JSON, но не является списком.
        """
        file_path = "../data/operations.json"
        not_a_list_json = {"transaction_id": 123, "value": 500}

        mock_os_exists.return_value = True
        mock_file_open.return_value.read.return_value = json.dumps(not_a_list_json)

        result = read_transactions(file_path)

        self.assertEqual(result, [])
        mock_os_exists.assert_called_once_with(file_path)
        mock_file_open.assert_called_once_with(file_path, "r", encoding="utf-8")

    # Более точный вариант для file_not_found, без использования assertRaises
    @patch("src.utils.os.path.exists")
    @patch("src.utils.open", side_effect=FileNotFoundError)  # Имитируем, что open выдаст ошибку
    def test_read_transactions_file_not_found_v2(self, mock_file_open, mock_os_exists):
        """
        Альтернативный тест для случая, когда файл не существует.
        """

        mock_os_exists.return_value = True

    @patch("src.utils.os.path.exists")
    def test_read_transactions_file_not_found_correct(self, mock_os_exists):
        """
        Корректный тест для случая, когда файл не существует.
        """
        file_path = "../data/non_existent_operations.json"

        mock_os_exists.return_value = False  # Файл не существует

        result = read_transactions(file_path)

        self.assertEqual(result, [])
        mock_os_exists.assert_called_once_with(file_path)
        # В этом случае 'open' не должен быть вызван, поэтому мы не будем его проверять.


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)


def test_process_bank_search(transaction_two):
    assert process_bank_search(transaction_two, "Открытие вклада") == [{
            "id": 587085106,
            "state": "EXECUTED",
            "date": "2018-03-23T10:45:06.972075",
            "operationAmount": {
                "amount": "48223.05",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Открытие вклада",
            "to": "Счет 41421565395219882431"
        }]


def test_process_bank_account_to_account(transaction_two):
    assert process_bank_search(transaction_two, "Перевод со счета на счет") == [{
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]

def test_process_bank_to_organisation(transaction_two):
    assert process_bank_search(transaction_two, "Перевод организации") == [{
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 41428829,
            "state": "EXECUTED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }]


def test_process_bank_operations(all_transactions):

    assert process_bank_operations(all_transactions) == Counter({'Перевод организации': 40,
             'Перевод с карты на карту': 19,
             'Перевод с карты на счет': 16,
             'Перевод со счета на счет': 15,
             'Открытие вклада': 10})