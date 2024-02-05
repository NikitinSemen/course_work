import json
import datetime


def get_data_json(file_name):
    with open(file_name) as file:
        operation = json.load(file)
        return operation


def get_new_operation(operation):
    oper_dict = []
    for i in operation:
        if i.get('state') == 'EXECUTED' and i.get('date'):
            oper_dict.append(i)
    return oper_dict


def get_sort_operation(operation_list):
    sorted_operation = sorted(operation_list, key=lambda operation: operation.get('date'), reverse=True)

    return sorted_operation


def get_five_operation(sorted_operation):
    return sorted_operation[0:5]


def get_format_date(date):
    split_date = date.split('T')[0]
    date_format = datetime.datetime.strptime(split_date, "%Y-%m-%d")
    new_date_time = date_format.strftime("%d-%m-%Y")
    return new_date_time


def mask_numb(number):
    return "**" + number[-4:]


def mask_number(number):
    return number[0:17] + "**** "

