from masks import get_mask_card_number, get_mask_account

def mask_account_card(number: str) -> str:
    number_digit = ''
    for symbol in number:
        if symbol.isdigit():
            number_digit += symbol
    if len(number_digit) == 16:
        mask_card_number = get_mask_card_number(number_digit)
        return f'{number[0:-16]}{mask_card_number}'
    elif len(number_digit) == 20:
        mask_card_number = get_mask_account(number_digit)
        return f'{number[0:-20]}{mask_card_number}'
    else:
        return 'У вас не карта, и не счёт!'



print(mask_account_card('Счферфе30135874305'))
