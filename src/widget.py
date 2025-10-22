from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_type_number: str) -> str:
    """Функция, которая умеет обрабатывать информацию как о картах, так и о счетах"""
    card_info = card_type_number.rsplit(" ", 1)
    if len(card_type_number) <= 16:
        raise ValueError("Номер карты некорректной длины")
    if not card_info[0].startswith("Счет"):
        masked_number = get_mask_card_number(card_info[1])
        return f"{card_info[0]} {masked_number}"
    else:
        masked_account = get_mask_account(card_info[1])
        return f"{card_info[0]} {masked_account}"


def get_date(datetime: str) -> str:
    """Функция, которая принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"""
    return f"{datetime[8:10]}.{datetime[5:7]}.{datetime[:4]}"
