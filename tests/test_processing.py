import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "list_dict, state",
    [
        ([{"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}], "EXECUTED"),
        ([{"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}], "CANCELED"),
    ],
)
def test_filter_by_state(list_dict: list[dict[str, any]], state) -> None:
    assert filter_by_state(list_dict, state) == [list_dict[0]]


def test_sort_by_date(list_dict, reverse=True) -> None:
    assert sort_by_date(list_dict, reverse) == list_dict
