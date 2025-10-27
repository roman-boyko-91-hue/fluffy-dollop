import logging
import os

# Реализация записей логов в файл
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler('../logs/masks.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')

file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str) -> str:
    """Функция маскировки номера банковской карты"""
    first_number = card_number[:6]
    last_number = card_number[-4:]
    avg_number = "** ****"
    try:
        logger.info("Маскировка номера банковской карты")
        return f"{first_number[:4]} {first_number[4:6]}{avg_number} {last_number}"
    except Exception:
        logger.error("Ошибка")


def get_mask_account(account_number: str) -> str:
    """Функция маскировки номера банковского счета"""
    first_number = "**"
    last_number = account_number[-4:]
    try:
        logger.info("Маскировка номера банковской карты")
        return f"{first_number}{last_number}"
    except Exception:
        logger.error("Ошибка")


result_1 = get_mask_card_number(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"))
result_2 = get_mask_account(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json"))
