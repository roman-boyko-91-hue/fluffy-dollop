import pytest


@pytest.fixture
def card_number():
    return "7020 7922 8960 6361"


@pytest.fixture
def card_result():
    return "7020 79** **** 6361"


@pytest.fixture
def filter_list_dict():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}]


@pytest.fixture
def list_dict():
    return [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
            {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
            ]
