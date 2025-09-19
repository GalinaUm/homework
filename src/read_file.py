import csv
from pprint import pprint
from typing import Any, Dict, List


import pandas as pd

def read_file_csv(file_name:str) -> list[Any] | None:
    """Функция для считывания финансовых операций. Принимает на вход файл.csv, возвращает список
        словарей"""

    try:
        with open(file_name, mode='r', encoding='utf-8') as file_csv:
            reader = csv.DictReader(file_csv, delimiter=';')
            result_dict = []
            for row in reader:
                result_dict.append(row)
            return result_dict
    except Exception as e:
        print(f'Ошибочка вышла {e}')
        return None
    except FileNotFoundError:
        print(f"Ошибка: Файл '{file_name}' не найден.")
        return None





if __name__ == '__main__':
    pprint(read_file_csv('../data/transactions.csv'))


def read_file_xlsx(file_name:str) -> List[Dict[Any, Any]]:
    """Функция для считывания финансовых операций. Принимает на вход файл.xlsx, возвращает список
    словарей"""

    reader = pd.read_excel(file_name)
    dict_reader = reader.to_dict(orient="records")
    return dict_reader

if __name__ == '__main__':
    pprint(read_file_xlsx('../data/transactions_excel.xlsx'))
