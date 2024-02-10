from utils.utils import (
    get_data_json,
    get_new_operation,
    get_format_date,
    get_five_operation,
    get_sort_operation,
    mask_number
)

path_file = "operations.json"
operation = get_data_json(path_file)
new_operation = get_new_operation(operation)
sort_operation = get_sort_operation(new_operation)
five_last_operation = get_five_operation(sort_operation)

for i in five_last_operation:
    print((''), get_format_date(i['date']), i['description'], '\n', mask_number(i.get('from', 'Новый счет')),
          "->", mask_number(i["to"]), "\n", i["operationAmount"]["amount"],
          i["operationAmount"]['currency']['name'], '\n\n')
