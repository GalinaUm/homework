def get_mask_card_number(number_card: int) -> str:
    """Функция, которая превращает номер карты в маску номера карты"""
    number_card_stroke = str(number_card)
    return f"{number_card_stroke[0:4]} {number_card_stroke[4:6]}** **** {number_card_stroke[12:]}"


def get_mask_account(number_account: int) -> str:
    """Функция, которая превращает номер счета в маску номера счета"""
    number_account_stroke = str(number_account)
    return f"**{number_account_stroke[16:]}"
