from typing import List, Dict, Any
import pandas as pd


def read_csv_transactions(file_path: str) -> List[Dict[str, Any]]:
    """cчитывает финансовые операции из CSV файла и возвращает список словарей"""
    try:
        df = pd.read_csv(file_path)
        return df.to_dict(orient="records")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {file_path} not found") from e
    except pd.errors.EmptyDataError as e:
        raise pd.errors.EmptyDataError("CSV file is empty") from e


def read_excel_transactions(file_path: str) -> List[Dict[str, Any]]:
    """считывает финансовые операции из Excel файла и возвращает список словарей"""
    try:
        df = pd.read_excel(file_path)
        return df.to_dict(orient="records")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File {file_path} not found") from e
    except ValueError as e:
        raise ValueError("Excel file is empty or invalid") from e
