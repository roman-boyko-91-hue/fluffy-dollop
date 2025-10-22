import pytest

from src.widget import get_date, mask_account_card


def test_invalid_length():
    with pytest.raises(ValueError):
        mask_account_card("")
        get_date("")
