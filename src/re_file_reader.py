from collections import Counter
import re


def filter_by_description(operations: list[dict], search_string: str) -> list[dict]:
    if not search_string.strip():
        return operations  # Если строка пустая, возвращаем все операции
    pattern = re.compile(re.escape(search_string.strip()), re.IGNORECASE)
    return [op for op in operations if pattern.search(op.get("description", ""))]


def count_by_category(operations: list[dict], categories: list[str]) -> dict:
    counter = Counter()

    for op in operations:
        description = op.get("description", "").lower()
        for category in categories:
            if category.lower() in description:
                counter[category] += 1  # Считаем категорию с исходным регистром

    # Возвращаем словарь с категориями в исходном виде и их счетчиками
    return {cat: counter[cat] for cat in categories}
