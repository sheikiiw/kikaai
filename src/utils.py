import json
import os


def load_transactions(file_path):
    if not os.path.exists(file_path):
        return []

    if os.path.getsize(file_path) == 0:
        return []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if isinstance(data, list):
                return data
            else:
                return []

    except (json.JSONDecodeError, ValueError):
        return []
