from src.processing import filter_by_state
from src.read_file import read_transactions_csv, read_transactions_excel
from src.utils import read_transactions



list_data_filepath = {1: "../data/operations.json",
                      2: "../data/transactions.csv",
                      3: "../data/transactions_excel.xlsx"}



def get_transaction_path() -> str:
    """
    Выбор типа транзакции
    """
    while True:
        messages = "Введите 1-3"
        try:
            print(messages)
            user_choice = int(input())
            if user_choice in list_data_filepath:
                file_path = str(list_data_filepath.get(user_choice))
                return file_path
        except ValueError:
            continue


def get_transaction_data(file_path: str, file_type: str) -> list[dict]:
    if file_type == "json":
        return read_transactions(file_path)
    if file_type == "csv":
        return read_transactions_csv(file_path)
    if file_type == "xlsx":
        return read_transactions_excel(file_path)
    return []

def state_approve() -> str:
    """
    Функция для проверки корректности ввода статуса
    """
    state_list = ["EXECUTED", "CANCELED","PENDING"]

    while True:
        messages = "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        print(messages)
        user_choice = input()
        if user_choice.upper() in state_list:
            current_state = user_choice.upper()
            return current_state
        else:
            print(f"Статус операции \"{user_choice}\" недоступен")




def main():
    """
    Функция которая отвечает за основную логику проекта и связывает функциональности между собой.
    """
    print("Добро пожаловать!")
    print("""Выберите необходимый пункт меню:
                    1. Получить информацию о транзакциях из JSON-файла
                    2. Получить информацию о транзакциях из CSV-файла
                    3. Получить информацию о транзакциях из XLSX-файла""")

    #Получаем путь файла и его тип
    transaction_path = get_transaction_path()
    transaction_file_type = transaction_path.rsplit('.', 1)[-1]

    print(f"Для обработки выбран {transaction_file_type} файл")

    data = get_transaction_data(transaction_path, transaction_file_type)

    print("Введите статус, по которому необходимо выполнить фильтрацию.")

    state = state_approve()
    print(f"Операции отфильтрованы по статусу \"{state}\"")

    data = filter_by_state(data, state)














print(main())





# def choose_transaction_type():
#     global data
#     print("""
#             Здравствуй, волшебник! Добро пожаловать в программу работы
#             с банковскими транзакциями банка Гринготтс.
#             Гоблины предлагают тебе выбрать необходимый пункт меню. Выбирай с умом,
#             иначе будешь подвергнут заклятью Круциатуса!:
#
#             1. Получить информацию о транзакциях из JSON-файла
#             2. Получить информацию о транзакциях из CSV-файла
#             3. Получить информацию о транзакциях из XLSX-файла
#             """)
#     wizard_num = int(input('Акалай-махалай, выбираю: '))
#
#     if wizard_num == 1:
#         data = read_transactions('data/operations.json')
#     elif wizard_num == 2:
#         data = read_transactions_csv('data/transactions.csv')
#     elif wizard_num == 3:
#         data = read_transactions_excel('data/transactions.xlsx')
#     else:
#         print('Ты че, Гарри Поттер? Авада кедавра!')
#     return data, wizard_num
#
#
#
# def main(*args):
#     """
#     Основная функция программы.
#     Выполняет последовательность загрузки данных, их очистки,
#     фильтрации и вывода итогового списка транзакций.
#     """
#
#     filtered_list = []
#
#     if args[0][1] == 1:
#         print('''Для обработки выбран JSON-файл. Сейчас вам предстоит узнать что-то
#                  o транзакциях Пожирателей смерти. Никому ничего не сообщайте, а то
#                  Темный Лорд вас покарает!''')
#         print('''Введите статус, по которому необходимо выполнить фильтрацию.
#                  Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING''')
#         status = input().lower()
#         data_list = args[0]
#
#         for item in data_list:
#             if data_list['state'].lower() == status:
#                 filtered_list.append(item)
#
#     return filtered_list






# if __name__ == '__main__':
#     print(main(choose_number))





