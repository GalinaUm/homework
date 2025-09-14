import json
import os
from typing import Any


def read_transactions(file_path: str) -> None | list[Any] | list:
    """Читает транзакции из файла"""
    if not os.path.exists(file_path):
        return []

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not data or not isinstance(data, list):
                return []
            return data
    except json.JSONDecodeError:
        print("Invalid JSON data.")

print(read_transactions("../data/operations.json"))

