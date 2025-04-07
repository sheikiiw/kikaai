import pytest
from src.widget import get_mask_card_number, get_mask_account, get_date

def test_get_mask_card_number_widget():
    assert get_mask_card_number("12345678901234567890") == "123456789012 3456 78 **** 90"
    assert get_mask_card_number("1234") == "1234  **** **** ****"
    assert get_mask_card_number("") == " **** **** **** ****"

def test_get_mask_account_widget():
    assert get_mask_account("12345678901234567890") == "7890"
    assert get_mask_account("1234") == "34"
    assert get_mask_account("") == ""

def test_get_date():
    assert get_date("2023-10-01") == "01.10.2023"
    assert get_date("2023-01-01") == "01.01.2023"
    assert get_date("") == ""