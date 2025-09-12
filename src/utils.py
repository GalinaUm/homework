import json
import os


def read_transactions(file_path: str) -> list[dict]:
    if not os.path.exists(file_path):
        return []

    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if not data or not isinstance(data, list):
            return []
        return data

# print(read_transactions('../data/operations.json'))