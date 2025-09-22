import pytest


@pytest.fixture
def coll():
    return 'data/test_transactions.csv', [{'amount': '16210',
                                           'currency_code': 'PEN',
                                           'currency_name': 'Sol',
                                           'date': '2023-09-05T11:30:32Z',
                                           'description': 'Перевод организации',
                                           'from': 'Счет 58803664561298323391',
                                           'id': '650703',
                                           'state': 'EXECUTED',
                                           'to': 'Счет 39745660563456619397'},
                                          {'amount': '29740',
                                           'currency_code': 'COP',
                                           'currency_name': 'Peso',
                                           'date': '2020-12-06T23:00:58Z',
                                           'description': 'Перевод с карты на карту',
                                           'from': 'Discover 3172601889670065',
                                           'id': '3598919',
                                           'state': 'EXECUTED',
                                           'to': 'Discover 0720428384694643'}]


@pytest.fixture
def transaction():
    return {
        "id": 518707726,
        "state": "EXECUTED",
        "date": "2018-11-29T07:18:23.941293",
        "operationAmount": {
            "amount": "3348.98",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        }}
