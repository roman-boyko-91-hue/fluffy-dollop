from database import create_database

from src.api_hh import load_and_save_data
from src.table_BD import create_tables

if __name__ == "__main__":
    create_database()
    create_tables()
    COMPANY_NAMES = [
        "Яндекс", "Сбер", "Т-Банк", "VK", "Ozon",
        "Авито", "Kaspersky", "МТС", "Альфа-Банк", "X5 Group"
    ]
    load_and_save_data(COMPANY_NAMES)
