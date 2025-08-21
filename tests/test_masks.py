import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def number_card():
    return 7000792289606361


@pytest.mark.parametrize("expected", ["7000 79** **** 6361"])
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected

def test_get_mask_card_number_wrong_length():
    with pytest.raises(ValueError):
        get_mask_card_number(7000792289606361123)







