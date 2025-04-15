import json
from typing import List, Dict, Any


def read_json_file(file_path: str) -> List[Dict[str, Any]]:
    """Читает JSON-файл и возвращает список словарей с данными о транзакциях.
    Если файл пустой, не найден или содержит не список, возвращает пустой список"""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, json.JSONDecodeError):
        return []
