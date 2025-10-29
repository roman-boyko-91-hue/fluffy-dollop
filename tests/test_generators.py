import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_card_number_generator():
    """Тестирование функции с ожидаемым результатом"""
    assert list(card_number_generator(1, 1))[0] == "0000 0000 0000 0001"


def test_trans_descriptions(description_result):
    """Тестирование функции с ожидаемым результатом"""
    transaction = [{"id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount":
                        {"amount": "9824.07",
                         "currency": {
                             "name": "USD",
                             "code": "USD"}
                         },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702"},
                   {"id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {
                            "name": "USD",
                            "code": "USD"}
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188"}]
    trans = transaction_descriptions(transaction)
    assert ", ".join(list(trans)) == description_result


def test_transaction_descriptions():
    """Тестирование функции с пустым списком"""
    assert list(transaction_descriptions([])) == []


def test_filter_by_currency_raises_value_error():
    """Тестирование выбрасываемого исключения"""
    transaction = [
        {"id": 1,
         "state": "EXECUTED",
         "date": "2018-06-30T02:08:58.425572",
         "operationAmount":
             {"amount": "3"}
         },
    ]
    with pytest.raises(ValueError) as exc_info:
        list(filter_by_currency(transaction, "USD"))
    assert "Некорректные данные в транзакции" in str(exc_info.value)


@pytest.mark.parametrize('result, expected', [
    (list(transaction_descriptions([])), []),
    (list(transaction_descriptions([
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }
    ])), ["Перевод организации", "Перевод со счета на счет"])
])
def test_transaction_descriptions_1(result, expected):
    """Тестирование функции с ожидаемым результатом"""
    assert sorted(result) == sorted(expected)


def test_card_num_generators(card_num):
    """Тестирование функции на корректность длины номера карт и состоят ли номера из цифр"""
    assert len(card_num) == 16
    assert card_num.isdigit()
