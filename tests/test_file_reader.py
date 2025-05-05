# tests/test_file_reader.py
from typing import List, Dict, Any
from unittest.mock import patch, MagicMock
import pytest
import pandas as pd
from src.file_reader import read_csv_transactions, read_excel_transactions


@pytest.fixture
def sample_transactions() -> List[Dict[str, Any]]:
    """cоздает тестовые данные с примерами финансовых транзакций"""
    return [
        {"id": 1, "amount": 100.0, "date": "2023-01-01"},
        {"id": 2, "amount": 200.0, "date": "2023-01-02"},
    ]


@patch("pandas.read_csv")
def test_read_csv_transactions_success(mock_read_csv: MagicMock, sample_transactions: List[Dict[str, Any]]) -> None:
    """проверяет успешное считывание транзакций из CSV файла"""
    mock_read_csv.return_value = pd.DataFrame(sample_transactions)
    result = read_csv_transactions("dummy.csv")
    assert result == sample_transactions
    mock_read_csv.assert_called_once_with("dummy.csv")


@patch("pandas.read_csv")
def test_read_csv_transactions_file_not_found(mock_read_csv: MagicMock) -> None:
    """проверяет обработку ошибки, когда CSV файл не найден"""
    mock_read_csv.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError, match="File dummy.csv not found"):
        read_csv_transactions("dummy.csv")


@patch("pandas.read_csv")
def test_read_csv_transactions_empty_file(mock_read_csv: MagicMock) -> None:
    """проверяет обработку ошибки, когда CSV файл пустой"""
    mock_read_csv.side_effect = pd.errors.EmptyDataError
    with pytest.raises(pd.errors.EmptyDataError, match="CSV file is empty"):
        read_csv_transactions("dummy.csv")


@patch("pandas.read_excel")
def test_read_excel_transactions_success(mock_read_excel: MagicMock,
                                         sample_transactions: List[Dict[str, Any]]) -> None:
    """проверяет успешное считывание транзакций из Excel файла"""
    mock_read_excel.return_value = pd.DataFrame(sample_transactions)
    result = read_excel_transactions("dummy.xlsx")
    assert result == sample_transactions
    mock_read_excel.assert_called_once_with("dummy.xlsx")


@patch("pandas.read_excel")
def test_read_excel_transactions_file_not_found(mock_read_excel: MagicMock) -> None:
    """проверяет обработку ошибки, когда Excel файл не найден"""
    mock_read_excel.side_effect = FileNotFoundError
    with pytest.raises(FileNotFoundError, match="File dummy.xlsx not found"):
        read_excel_transactions("dummy.xlsx")


@patch("pandas.read_excel")
def test_read_excel_transactions_empty_file(mock_read_excel: MagicMock) -> None:
    """проверяет обработку ошибки, когда Excel файл пустой или некорректный"""
    mock_read_excel.side_effect = ValueError
    with pytest.raises(ValueError, match="Excel file is empty or invalid"):
        read_excel_transactions("dummy.xlsx")
