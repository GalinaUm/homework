import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("../logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(number_card: int) -> str:
    """Функция, которая превращает номер карты в маску номера карты"""

    logger.warning(f"Номер {number_card} неправильный")
    if len(str(number_card)) != 16:
        logger.error("Произошла ошибка")
        raise ValueError("Неправильная длина номера")

    logger.info(f"Создается маска для номера карты {number_card}")
    number_card_string = str(number_card)
    return f"{number_card_string[0:4]} {number_card_string[4:6]}** **** {number_card_string[12:]}"


def get_mask_account(number_account: int) -> str:
    """Функция, которая превращает номер счета в маску номера счета"""

    logger.warning(f"Номер {number_account} неправильный")
    if len(str(number_account)) != 20:
        logger.error("Произошла ошибка")
        raise ValueError("Неправильная длина номера")

    logger.info(f"Создается маска для номера аккаунта {number_account}")
    number_account_stroke = str(number_account)
    return f"**{number_account_stroke[16:]}"


print(get_mask_account(4562378546))
