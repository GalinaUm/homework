import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def number_card() -> int:
    return 7000792289606361


@pytest.mark.parametrize("expected", ["7000 79** **** 6361"])
def test_get_mask_card_number(number_card: int, expected: str) -> None:
    assert get_mask_card_number(number_card) == expected


def test_get_mask_card_number_wrong_length() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number(7000792289606361123)


@pytest.mark.parametrize(
    "number_card, expected", [(6831982476737658, "6831 98** **** 7658"), (7000792289606361, "7000 79** **** 6361")]
)
def test_get_mask_card_number_change(number_card: int, expected: str) -> None:
    assert len(str(number_card)) + 3 == len(expected)


@pytest.fixture
def number_account() -> int:
    return 73654108430135874305


@pytest.mark.parametrize("expected", ["**4305"])
def test_get_mask_account(number_account: int, expected: str) -> None:
    assert get_mask_account(number_account) == expected


def test_get_mask_account_wrong_length() -> None:
    with pytest.raises(ValueError):
        get_mask_account(73654108430135874305123)
