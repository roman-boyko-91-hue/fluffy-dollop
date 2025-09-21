def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    card_number = card_number.replace(" ", "")
    if len(card_number) != 16:
        raise ValueError("Номер карты некорректной длины")
    first_number = card_number[:6]
    last_number = card_number[-4:]
    avg_number = "** ****"
    return f"{first_number[:4]} {first_number[4:6]}{avg_number} {last_number}"


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    account_number = account_number.replace(" ", "")
    if len(account_number) != 20:
        raise ValueError("Номер аккаунта некорректной длины")
    first_number = "**"
    last_number = account_number[-4:]
    return f"{first_number}{last_number}"
