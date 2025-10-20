import json
import os

import pandas as pd

from src.func_for_main import filter_by_state, sort_by_date
from src.description import search_transactions

file_name = r"../data/transactions.csv"
file_path = r"../data/transactions_excel.xlsx"
file_operation = r"../data/operations.json"


def get_yes_no_input(prompt):
    while True:
        answer = input(prompt).strip().lower()
        if answer in ['да', 'нет']:
            return answer == 'да'
        else:
            print('Программа: Пожалуйста, введите "Да" или "Нет".')


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
            with open(file_operation, "r", encoding='utf-8') as file:
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
        print("Отфильтрованные и отсортированные транзакции по дате:")
        for transaction in transactions:
            print(transaction)
        order = input(
            "Программа: Сортировка по возрастанию или по убыванию? по возрастанию/по убыванию\n").strip().lower()
        transactions = sort_by_date(transactions, reverse=True)
        print("Отфильтрованные и отсортированные транзакции:")
        for transaction in transactions:
            print(transaction)

    if get_yes_no_input('Программа: Выводить только рублевые транзакции? Да/Нет'):
        for t in transactions:
            transactions = [t for t in transactions if t.get('operationAmount', {}).get('currency', {}).get('code') == 'RUB']
            print(transactions)


    word_filter = input("Программа: Отфильтровать по слову? Да/Нет\n").strip().lower()
    if word_filter in ['да', 'yes']:
        search = input("Программа: Введите слово для поиска:\n").strip().lower()
        transactions = search_transactions(transactions, search)

    print("Отфильтрованные и отсортированные транзакции:")
    for t in transactions:
        print(transactions)

    # Вывод результата

    print("Программа: Распечатываю итоговый список транзакций...")
    print(transactions)
    if not transactions:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Программа: Всего банковских операций в выборке: {len(transactions)}")


# Добавлен вызов main функции если файл запущен напрямую
if __name__ == "__main__":
    main()
