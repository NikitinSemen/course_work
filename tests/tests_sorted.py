from utils.utils import get_data_json
from utils.utils import get_new_operation
from utils.utils import get_sort_operation
from utils.utils import get_five_operation
import json


with open('file.json') as file:
    test_list = json.load(file)


def test_get_data_json():
    assert get_data_json('file.json') == test_list


new_dict = []
for i in test_list:
    if i.get('state') == 'EXECUTED' and i.get('date'):
        new_dict.append(i)


def test_get_new_operation():
    assert get_new_operation(test_list) == new_dict


sorted_operation = sorted(new_dict, key=lambda operation: operation.get('date'), reverse=True)


def test_get_sorted_operation():
    assert get_sort_operation(new_dict) == sorted_operation


operation = sorted_operation[0:5]


def test_get_five_operation():
    assert get_five_operation(sorted_operation) == operation
