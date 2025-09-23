from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Обрабатывает номер карты или номер счёта
    """
    is_card_number = False
    if "счет" not in account_card.lower().replace("ё", "e"):
        is_card_number = True

    account_card_arr = account_card.split()
    prefix_number = ""
    for word in account_card_arr:
        if word.isalpha():
            prefix_number = prefix_number + " " + word
        if word.isdigit():
            if is_card_number:
                card_number = get_mask_card_number(int(word))
                return prefix_number[1:] + " " + card_number
            else:
                account_number = get_mask_account((int(word)))
                return prefix_number[1:] + " " + account_number
    return "Информация неверна"


# def mask_account_card(number: str) -> str:
#     """Функция, которая создает маску номера или счета"""
#
#     number_digit = ""
#
#     for symbol in number:
#         if symbol.isdigit():
#             number_digit += symbol
#
#     number_digit_int = int(number_digit)
#
#     if len(number_digit) < 16:
#         raise ValueError("Неверный номер карты или счета")
#
#     if 16 < len(number_digit) < 20:
#         raise ValueError("Неверный номер карты или счета")
#
#     if len(number_digit) > 20:
#         raise ValueError("Неверный номер карты или счета")
#
#     if len(number_digit) == 16:
#         mask_card_number = get_mask_card_number(number_digit_int)
#         return f"{number[0:-16]}{mask_card_number}"
#
#     elif len(number_digit) == 20:
#         mask_card_number = get_mask_account(number_digit_int)
#         return f"{number[0:-20]}{mask_card_number}"
#
#     else:
#         return "У вас не карта, и не счёт!"


def get_date(date: str) -> str:
    """
    Возвращает дату из формата ГГГГ-ММ-ДД в ДД.ММ.ГГГГ
    """
    if len(date) <= 1:
        return "Дата не может быть пустой"
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    new_date = day + "." + month + "." + year

    try:
        datetime.strptime(new_date, "%d.%m.%Y")
        return new_date
    except ValueError:
        return date


print(mask_account_card("Visa Gold 5999414228426353"))
