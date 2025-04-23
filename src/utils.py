import unittest
from unittest.mock import Mock, patch

from src.external_api import convert, total_amount


class TestCurrencyConversion(unittest.TestCase):

    @patch("requests.get")
    def test_convert_success(self, mock_get):
        # Имитация успешного ответа от API
        mock_response = Mock()
        mock_response.json.return_value = {"result": 7500.0}
        mock_get.return_value = mock_response

        dict_transaction = {
            "operationAmount": {"currency": {"code": "USD"}, "amount": 100}
        }

        result = convert(dict_transaction)
        self.assertEqual(result, 7500.0)

    @patch("requests.get")
    def test_convert_failure(self, mock_get):
        # Имитация неудачного ответа от API
        mock_response = Mock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        dict_transaction = {
            "operationAmount": {"currency": {"code": "USD"}, "amount": 100}
        }

        result = convert(dict_transaction)
        self.assertIsNone(result)

    @patch("src.external_api.convert")
    def test_total_amount_with_rub(self, mock_convert):
        # Имитация транзакций в рублях
        mock_convert.return_value = None

        dict_transactions = [
            {"operationAmount": {"currency": {"code": "RUB"}, "amount": 100}},
            {"operationAmount": {"currency": {"code": "RUB"}, "amount": 200}},
        ]

        result = total_amount(dict_transactions)
        self.assertEqual(result, 300.0)

    @patch("src.external_api.convert")
    def test_total_amount_with_conversion(self, mock_convert):
        # Имитация транзакций с конвертацией
        mock_convert.side_effect = [7500.0, 15000.0]

        dict_transactions = [
            {"operationAmount": {"currency": {"code": "USD"}, "amount": 100}},
            {"operationAmount": {"currency": {"code": "EUR"}, "amount": 200}},
        ]

        result = total_amount(dict_transactions)
        self.assertEqual(result, 22500.0)

    def test_total_amount_empty_list(self):
        # Проверка пустого списка транзакций
        result = total_amount([])
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
