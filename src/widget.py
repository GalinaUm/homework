from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(number: str) -> str:
    """Функция, которая создает маску номера или счета"""


    number_digit = ""

    for symbol in number:
        if symbol.isdigit():
            number_digit += symbol

    number_digit_int = int(number_digit)

    if len(number_digit) < 16:
        raise ValueError('Неверный номер карты или счета')

    if 16 < len(number_digit) < 20:
        raise ValueError('Неверный номер карты или счета')

    if len(number_digit) > 20:
        raise ValueError('Неверный номер карты или счета')

    if len(number_digit) == 16:
        mask_card_number = get_mask_card_number(number_digit_int)
        return f"{number[0:-16]}{mask_card_number}"

    elif len(number_digit) == 20:
        mask_card_number = get_mask_account(number_digit_int)
        return f"{number[0:-20]}{mask_card_number}"

    else:
        return "У вас не карта, и не счёт!"


def get_date(date_unformatted: str) -> str:
    """Функция, которая форматирует дату"""
    date_cut_list = date_unformatted[:10].split("-")
    return ".".join([date_cut_list[1], date_cut_list[2], date_cut_list[0]])


print(mask_account_card("Maestro 1596837868705199"))
