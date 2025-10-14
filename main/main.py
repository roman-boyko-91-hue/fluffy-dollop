import os
import pandas as pd
import json
from os import path

file_path = r"C:\Users\1\PycharmProjects\pythonProject\transactions_excel.xlsx"
transactions_df = pd.read_excel(file_path)
transactions_list = transactions_df.to_dict(orient='records')


def main():
    """
    Функция, которая отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print('Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
    print('Выберите необходимый пункт меню:')
    print('1. Получить информацию о транзакциях из JSON-файла')
    print('2. Получить информацию о транзакциях из CSV-файла')
    print('3. Получить информацию о транзакциях из XLSX-файла')

    while True:
        choice = input('Пользователь: ').strip()
        if choice == '1':
            print('Программа: Для обработки выбран JSON-файл.')
            transactions = json.load(os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
            break
        elif choice == '2':
            print('Программа: Для обработки выбран CSV-файл.')
            transactions = load_csv_file(
                path.join(path.dirname(path.dirname(__file__)), "data", "transactions.csv"))
            break
        elif choice == '3':
            print('Программа: Для обработки выбран XLSX-файл.')
            transactions = load_exel_file(
                path.join(path.dirname(path.dirname(__file__)), "data", "transactions_excel.xlsx"))
            break
        else:
            print('Программа: Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.')

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


while True:
    print('Программа: Отсортировать операции по дате? Да/Нет')
    sort_answer = input('Пользователь: ').strip().lower()
    if sort_answer in ['да', 'нет']:
        break
    else:
        print('Программа: Пожалуйста, введите "Да" или "Нет".')

if sort_answer == 'да':
    while True:
        print('Программа: Отсортировать по возрастанию или по убыванию?')
        order = input('Пользователь: ').strip().lower()
        if order in ['по возрастанию', 'по убыванию']:
            descending = (order == 'по возрастанию')
            transactions = sort_by_date(transactions, descending)
            break
        else:
            print('Программа: Пожалуйста, введите "по возрастанию" или "по убыванию".')

while True:
    print('Программа: Выводить только рублевые транзакции? Да/Нет')
    rub_filter = input('Пользователь: ').strip().lower()
    if rub_filter in ['да', 'нет']:
        break
    else:
        print('Программа: Пожалуйста, введите "Да" или "Нет".')

if rub_filter == 'да':
    transactions = filter_by_currency(transactions, 'RUB')

while True:
    print('Программа: Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
    keyword_filter = input('Пользователь: ').strip().lower()
    if keyword_filter in ['да', 'нет']:
        break
    else:
        print('Программа: Пожалуйста, введите "Да" или "Нет".')

if keyword_filter == 'да':
    print('Программа: Введите слово для фильтрации:')
    keyword = input('Пользователь: ').strip()
    transactions = process_bank_search(transactions, keyword)

print('Программа: Распечатываю итоговый список транзакций...\n')
print(f"Всего банковских операций в выборке: {process_bank_operations}")
return transactions
