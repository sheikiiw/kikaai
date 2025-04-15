from unittest.mock import patch, mock_open
from src.utils import read_json_file
from src.external_api import convert_to_rub


def test_read_json_file_valid():
    mock_data = '[{"id": 1, "amount": 100, "currency": "USD"}]'
    with patch('builtins.open', mock_open(read_data=mock_data)):
        result = read_json_file('dummy_path.json')
        assert result == [{"id": 1, "amount": 100, "currency": "USD"}]


def test_read_json_file_empty():
    with patch('builtins.open', mock_open(read_data='[]')):
        result = read_json_file('dummy_path.json')
        assert result == []


def test_convert_to_rub_rub_currency():
    transaction = {"amount": 1000, "currency": "RUB"}
    assert convert_to_rub(transaction) == 1000.0


@patch('requests.get')
def test_convert_to_rub_usd(mock_get):
    mock_get.return_value.json.return_value = {"rates": {"RUB": 90.0}}
    transaction = {"amount": 100, "currency": "USD"}
    result = convert_to_rub(transaction)
    assert result == 9000.0
