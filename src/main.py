import pandas as pd

from views import main
from services import cashback_analyze
from reports import spending_by_category

if __name__ == "__main__":
    date = "2020-04-11 12:00:00"
    result_view = main(date)
    # print(result_view)
    result_sevices = cashback_analyze("../data/operations.xlsx", 2018, 3)

    df = pd.read_excel("../data/operations.xlsx", sheet_name="Отчет по операциям")
    transactions = df.to_dict(orient='records')
    result_reports = spending_by_category(df, "Ж/д билеты", "2020-04-11")
    print(result_sevices)
