import json
import logging
import os
import re
from pprint import pprint
from typing import Any
from collections import Counter, defaultdict

from src.read_file import read_transactions_csv

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("F:/Galina/_python/_homework/logs/masks.log")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> None | list[Any] | list:
    """Читает транзакции из файла"""

    if not os.path.exists(file_path):
        logger.info("Файла не существует или он пустой")
        return []

    try:
        logger.info("Данные считываются из файла")
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not data or not isinstance(data, list):
                return []
            return data
    except json.JSONDecodeError:
        logger.error("Данные имеют неправильный вид")
        print("Invalid JSON data.")


my_dict = read_transactions("../data/operations.json")



def process_bank_search(data_dict: list[dict], description: str | None = "Перевод с карты на счет") -> list[
    dict]:
    """
        Фильтрует список банковских операций, оставляя только те,
        в описании которых содержится указанная строка поиска.
        """
    pattern = re.compile(re.escape(description), re.IGNORECASE)

    result = []
    for operation in data_dict:

        desc = str(operation.get("description", ""))
        if pattern.search(desc):
            result.append(operation)
    return result


# pprint(process_bank_search(my_dict, "Перевод с карты на счет"))


def process_bank_operations(data: list[dict], categories:list='') -> dict:
    """
    Принимает список словарей с данными о банковских операциях и список категорий операций,
    возвращает словарь, в котором ключи — это названия категорий,
    а значения — это количество операций в каждой категории.
    """
    if not categories:
        my_list = []

        for data_dict in data:
            for key, val in data_dict.items():
                if key == 'description':
                    my_list.append(val)

        my_list_after_count = Counter(my_list)

        return my_list_after_count

    else:
        my_list = []

        for data_dict in data:
            for key, val in data_dict.items():
                if key == 'description' and val in categories:
                    my_list.append(val)

        my_list_after_count = Counter(my_list)

        return my_list_after_count

if __name__ == '__main__':
    pprint(process_bank_operations(my_dict))








    # result = {c: 0 for c in categories}
    # for tran in data:
    #     desc = tran['description']
    #     result[desc] += 1
    # return result


