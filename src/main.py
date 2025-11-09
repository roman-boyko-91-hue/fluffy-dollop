from views import main
from services import cashback_analyze

if __name__ == "__main__":
    date = "2020-04-11 12:00:00"
    result_view = main(date)
    #print(result_view)
    result_sevices = cashback_analyze("../data/operations.xlsx", 2018, 3)
    print(result_sevices)
