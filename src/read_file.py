import os
from typing import Dict, List

import pandas as pd


def read_transactions_csv(path: str) -> List[Dict]:
    """
    Считывает финансовые операции из CSV-файла.

    """
    df = pd.read_csv(path)
    return df.to_dict(orient="records")


def read_transactions_excel(path: str) -> List[Dict]:
    """
    Считывает финансовые операции из Excel-файла.

    """
    df = pd.read_excel(path)
    return df.to_dict(orient="records")


# --- Ниже код, который выполняется сразу при запуске скрипта ---

# Определяем абсолютный путь к текущей папке файла

# в начале работы раскомментирровать ---------------------
# base_dir = os.path.dirname(os.path.abspath(__file__))
# data_dir = os.path.abspath(os.path.join(base_dir, "..", "data"))
#
# csv_path = os.path.join(data_dir, "transactions.csv")
# excel_path = os.path.join(data_dir, "transactions_excel.xlsx")
#
# # Чтение и вывод транзакций из CSV
# try:
#     transactions_csv = read_transactions_csv(csv_path)
#     print("Транзакции из CSV:")
#     for t in transactions_csv:
#         print(t)
# except FileNotFoundError:
#     print(f"Файл CSV не найден по пути: {csv_path}")
#
# print("\n" + "-" * 40 + "\n")
#
# # Чтение и вывод транзакций из Excel
# try:
#     transactions_excel = read_transactions_excel(excel_path)
#     print("Транзакции из Excel:")
#     for t in transactions_excel:
#         print(t)
# except FileNotFoundError:
#     print(f"Файл Excel не найден по пути: {excel_path}")

# --------------------------------------------------


# import csv
# from pprint import pprint
# from typing import Any, Dict, List
#
#
# import pandas as pd
#
# def read_file_csv(file_name:str) -> list[Any] | None:
#     """Функция для считывания финансовых операций. Принимает на вход файл.csv, возвращает список
#         словарей"""
#
#     try:
#         with open(file_name, mode='r', encoding='utf-8') as file_csv:
#             reader = csv.DictReader(file_csv, delimiter=';')
#             result_dict = []
#             for row in reader:
#                 result_dict.append(row)
#             return result_dict
#     except FileNotFoundError:
#         print(f"Ошибка: Файл '{file_name}' не найден.")
#         raise FileNotFoundError
#     except Exception as e:
#         print(f'Ошибочка вышла {e}')
#         raise e

#
#
#
#
#
# if __name__ == '__main__':
#     pprint(read_file_csv('../data/transactions.csv'))
#
#
# def read_file_xlsx(file_name:str) -> List[Dict[Any, Any]]:
#     """Функция для считывания финансовых операций. Принимает на вход файл.xlsx, возвращает список
#     словарей"""
#
#     reader = pd.read_excel(file_name)
#     dict_reader = reader.to_dict(orient="records")
#     return dict_reader
#
# if __name__ == '__main__':
#     pprint(read_file_xlsx('../data/transactions_excel.xlsx'))
