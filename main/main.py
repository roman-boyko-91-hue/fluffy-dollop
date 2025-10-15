import json
import os

import pandas as pd

from src.func_for_main import filter_by_state, sort_by_date

file_name = r"C:\Users\1\PycharmProjects\pythonProject\transactions.csv"
file_path = r"C:\Users\1\PycharmProjects\pythonProject\transactions_excel.xlsx"


def main():
    """
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print('Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')

    transactions = []

    while True:
        choice = input('Пользователь: ').strip()
        if choice == '1':
            print('Программа: Для обработки выбран JSON-файл.')
            with open(os.path.join("C:\Users\1\PycharmProjects\pythonProject\main\operations.json"), 'r') as file:
                transactions = json.load(file)
            break
        elif choice == '2':
            print('Программа: Для обработки выбран CSV-файл.')
            transactions_df = pd.read_csv(file_name)
            transactions = transactions_df.to_dict(orient='records')
            break
        elif choice == '3':
            print('Программа: Для обработки выбран XLSX-файл.')
            transactions_df = pd.read_excel(file_path)
            transactions = transactions_df.to_dict(orient='records')
            break
        else:
            print('Программа: Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.')

    if not transactions:
        print("Программа: Ошибка загрузки данных. Проверьте источник данных.")
        return

    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        print('Программа: Введите статус, по которому необходимо выполнить фильтрацию.')
        print(f'Доступные для фильтрации статусы: {", ".join(valid_statuses)}')
        status_input = input('Пользователь: ').strip()
        if status_input.upper() in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status_input.upper()}"')
            transactions = filter_by_state(transactions, status_input)
            break
        else:
            print(f'Программа: Статус операции "{status_input}" недоступен.')

    if get_yes_no_input('Программа: Отсортировать операции по дате? Да/Нет'):
        order = get_yes_no_input('Программа: Сортировка по возрастанию или по убыванию?')
        transactions = sort_by_date(transactions, reverse=not order)

    if get_yes_no_input('Программа: Выводить только рублевые транзакции? Да/Нет'):
        transactions = filter_by_state(transactions, 'RUB')

    print('Программа: Распечатываю итоговый список транзакций...\n')
    print(f"Всего банковских операций в выборке: {len(transactions)}")


def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['да', 'нет']:
            return answer == 'да'
        else:
            print('Программа: Пожалуйста, введите "Да" или "Нет".')
