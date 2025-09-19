import os
import unittest
from unittest.mock import patch, mock_open, MagicMock

import pytest
import requests
import json

from src.read_file import read_file_csv


# @pytest.fixture()
# def coll():
#     return [{'amount': '16210',
#              'currency_code': 'PEN',
#              'currency_name': 'Sol',
#              'date': '2023-09-05T11:30:32Z',
#              'description': 'Перевод организации',
#              'from': 'Счет 58803664561298323391',
#              'id': '650703',
#              'state': 'EXECUTED',
#              'to': 'Счет 39745660563456619397'},
#             {'amount': '29740',
#              'currency_code': 'COP',
#              'currency_name': 'Peso',
#              'date': '2020-12-06T23:00:58Z',
#              'description': 'Перевод с карты на карту',
#              'from': 'Discover 3172601889670065',
#              'id': '3598919',
#              'state': 'EXECUTED',
#              'to': 'Discover 0720428384694643'}]
#
# @pytest.fixture()
# def test_read_file_csv(file_name, expected):
#     file_name = '../data/test_transactions.csv'
#     assert read_file_csv(file_name) == expected


def test_read_file_csv_errors():
    with pytest.raises(Exception) as exc_info:
        read_file_csv('fghjfghadhg')
        assert  exc_info == "Ошибочка вышла [Errno 2] No such file or directory: 'fghjfghadhg'"
