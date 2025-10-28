from src.utils import get_transactions_from_json
from src.transactions_csv import read_file_csv
from src.transactions_excel import open_transaction_excel
from src.processing import filter_by_state, sort_by_date
from src.generators import filter_by_currency
from src.description import search_transactions
from masks import get_mask_card_number
from widget import get_date, mask_account_card

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
            transactions = get_transactions_from_json(file_operation)
            break
        elif choice == '2':
            print('Программа: Для обработки выбран CSV-файл.')
            transactions = read_file_csv(file_name)
            break
        elif choice == '3':
            print('Программа: Для обработки выбран XLSX-файл.')
            transactions = open_transaction_excel(file_path)
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
        status_input = input('Пользователь: ').strip().upper()
        if status_input.upper() in valid_statuses:
            print(f'Программа: Операции отфильтрованы по статусу "{status_input}"')
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
        if order == "по убыванию":
            transactions = sort_by_date(transactions, reverse=True)
        else:
            transactions = sort_by_date(transactions, reverse=False)
        print("Отфильтрованные и отсортированные транзакции:")
        for transaction in transactions:
            print(transaction)

    if get_yes_no_input('Программа: Выводить только рублевые транзакции? Да/Нет'):
        transactions = list(filter_by_currency(transactions, "RUB"))
        print(transactions)

    word_filter = input("Программа: Отфильтровать по слову? Да/Нет\n").strip().lower()
    if word_filter in ['да', 'yes']:
        search = input("Программа: Введите слово для поиска:\n").strip().lower()
        transactions = search_transactions(transactions, search)

    print("Отфильтрованные и отсортированные транзакции:")
    for t in transactions:
        print(t)

    print("Программа: Распечатываю итоговый список транзакций...\n")
    print("Всего банковских операций в выборке: {}".format(len(transactions)))

    masked_transactions = get_mask_card_number('card_number')
    print(masked_transactions[:])

    for transaction in transactions:
        print(f"{get_date(transaction['date'])} {transaction['description']}")
        if 'from' in transaction and 'to' in transaction:
            print(f"{mask_account_card(transaction['from'])} -> {mask_account_card(transaction['to'])}")
        elif 'from' in transaction:
            print(mask_account_card(transaction['from']))
        elif 'to' in transaction:
            print(mask_account_card(transaction['to']))
        print(f"Сумма: {transaction['operationAmount']['amount']} {transaction['operationAmount']['currency']['name']}")

        if not transactions:
            print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return


if __name__ == "__main__":
    main()
