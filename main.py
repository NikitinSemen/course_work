from utils import get_data_json
from utils import get_new_operation
from utils import get_sort_operation
from utils import get_five_operation
from utils import get_format_date
from utils import vanish_from
from utils import vanish
import datetime

operation = get_data_json("operations.json")
new_operation = get_new_operation(operation)
sort_operation = get_sort_operation(new_operation)
five_last_operation = get_five_operation(sort_operation)




for i in five_last_operation:

    print(get_format_date(i['date']), i['description'], '\n', vanish_from(i.get('from', 'Новый счет')),
          "->", vanish(i["to"]), "\n", i["operationAmount"]["amount"], '\n\n')

