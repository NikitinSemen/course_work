import json
import datetime


def get_data_json(file_name):
    """функция получает файл json декодирует под python"""
    with open(file_name) as file:
        operation = json.load(file)
        return operation


def get_new_operation(operation):
    """ Исключает неподходящие операции для вывода"""
    oper_dict = []
    for i in operation:
        if i.get('state') == 'EXECUTED' and i.get('date'):
            oper_dict.append(i)
    return oper_dict


def get_sort_operation(operation_list):
    """ сортирует операции по дате"""
    return sorted(operation_list, key=lambda operation: operation.get('date'), reverse=True)


def get_five_operation(sorted_operation):
    """получает пять последних операций"""
    return sorted_operation[0:5]


def get_format_date(date):
    """меняет формат даты на %Y-%m-%d"""
    split_date = date.split('T')[0]
    date_format = datetime.datetime.strptime(split_date, "%Y-%m-%d")
    new_date_time = date_format.strftime("%d.%m.%Y")
    return new_date_time


def mask_numb(number):
    """ маскирует номер карты получения"""
    numb_split = number.split(' ')[-1]
    name_chek = number.split(' ')[0]
    return f' {name_chek} {"**" + numb_split[-4:]}'


def mask_number(num):
    """ маскирует номер карты отправителя"""

    if num == 'Новый счет':
        return 'Новый счет'
    card = num.split()[-1]
    private_number = card[:4] + (len(card[6:-4]) * '*') + card[-4:]
    return f'{num.split()[0]} {private_number}'
