import json
import os
from typing import Any
import datetime
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions(file_path: str) -> None | list[Any] | list:
    """Читает транзакции из файла"""


    if not os.path.exists(file_path):
        logger.info('Файла не существует или он пустой')
        return []

    try:
        logger.info('Данные считываются из файла')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            if not data or not isinstance(data, list):
                return []
            return data
    except json.JSONDecodeError:
        logger.error('Данные имеют неправильный вид')
        print("Invalid JSON data.")

print(read_transactions("../data/operations.json"))

