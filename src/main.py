import pandas as pd

from views import main
from services import cashback_analyze
from reports import spending_by_category

if __name__ == "__main__":
    date = "2020-04-11 12:00:00"
    result_view = main(date)
    # print(result_view)

    df = pd.read_excel("../data/operations.xlsx", sheet_name="Отчет по операциям")
    transactions = df.to_dict(orient='records')
    result_services = cashback_analyze(transactions, year=2018, month=3)
    print(result_services)
