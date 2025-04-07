import pytest
from src.masks import get_mask_card_number, get_mask_account

def test_get_mask_card_number():
    assert get_mask_card_number("1234567812345678") == "1234 56** **** 5678"
    assert get_mask_card_number("1234") == "1234 **** **** ****"
    assert get_mask_card_number("") == "**** **** **** ****"
    assert get_mask_card_number("123456789012345") == "1234 56** **** 2345"

def test_get_mask_account():
    assert get_mask_account("12345678901234567890") == "**7890"
    assert get_mask_account("1234") == "**34"
    assert get_mask_account("") == "**"