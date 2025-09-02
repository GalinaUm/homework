def get_mask_card_number(number_card: int) -> str:
    """Функция, которая превращает номер карты в маску номера карты"""

    if len(str(number_card)) != 16:
        raise ValueError("Неправильная длина номера")

    number_card_string = str(number_card)
    return f"{number_card_string[0:4]} {number_card_string[4:6]}** **** {number_card_string[12:]}"


def get_mask_account(number_account: int) -> str:
    """Функция, которая превращает номер счета в маску номера счета"""

    if len(str(number_account)) != 20:
        raise ValueError("Неправильная длина номера")

    number_account_stroke = str(number_account)
    return f"**{number_account_stroke[16:]}"
