import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "account_number, expected",
    [("12345678901234567890", "**7890"), ("41151341151341165478", "**5478"), ("46848434385465413543", "**3543")],
)
def test_get_mask_account(account_number, expected) -> None:
    assert get_mask_account(account_number) == expected


def test_get_mask_card_number(card_number, card_result):
    assert get_mask_card_number(card_number) == card_result


def test_invalid_length():
    with pytest.raises(ValueError):
        get_mask_account("13134154845")
        get_mask_account("")
        get_mask_card_number("")
