import pytest

from src.widget import mask_account_card, get_date
from src.masks import get_mask_account, get_mask_card_number




@pytest.mark.parametrize("account, expected", [("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                                              ("Счет 64686473678894779589", "Счет **9589"),
                                              ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                                              ("Счет 35383033474447895560", "Счет **5560"),
                                              ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                                              ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                                              ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                                              ("Счет 73654108430135874305", "Счет **4305")])
def test_mask_account_card(account, expected):
    assert mask_account_card(account) == expected


def test_mask_account_card_invalid_card_number_less():
    with pytest.raises(ValueError):
        mask_account_card("Maestro 159683786")


def test_mask_account_card_invalid_card_number_more():
    with pytest.raises(ValueError):
        mask_account_card("Maestro 1596837868705199618")


def test_mask_account_card_invalid_account_number_less():
    with pytest.raises(ValueError):
        mask_account_card("Счет 736541084301358743")


def test_mask_account_card_invalid_account_number_more():
    with pytest.raises(ValueError):
        mask_account_card("Счет 73654108430135874645216853")














