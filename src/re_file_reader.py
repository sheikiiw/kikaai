import re

from collections import Counter


def filter_by_description(operations: list[dict], search_string: str) -> list[dict]:
    pattern = re.compile(re.escape(search_string), re.IGNORECASE)
    return [op for op in operations if pattern.search(op.get("description", ""))]


def count_by_category(operations: list[dict], categories: list[str]) -> dict:
    normalized_categories = [cat.lower() for cat in categories]
    counter = Counter()

    for op in operations:
        description = op.get("description", "").lower()
        for category in normalized_categories:
            if category in description:
                counter[category] += 1

    result = {cat: counter[cat.lower()] for cat in categories}
    return result
