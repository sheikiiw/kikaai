from typing import List, Dict, Any

from datetime import datetime


def filter_by_state(data: List[Dict[str, Any]], state: str = "EXECUTED") -> List[Dict[str, Any]]:
    """Фильтрует список словарей по значению ключа state"""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """Сортирует список словарей по значению ключа date"""
    return sorted(
        data, key=lambda x: datetime.fromisoformat(x["date"]), reverse=descending)
