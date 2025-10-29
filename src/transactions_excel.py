import pandas as pd

file_path = r"C:\Users\1\PycharmProjects\pythonProject\transactions_excel.xlsx"


def open_transaction_excel(file_path):
    """Функция для считывания финансовых операций из Excel - файла,
    принимает путь к файлу Excel в качестве аргумента и выдает список
    словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        print(df.head())
        return df.to_dict(orient='records')
    except Exception:
        return []
