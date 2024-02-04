import json
import datetime

file_name = "operations.json"
with open(file_name) as file:
    operation = json.load(file)

    for i in operation:
        print(i['date'].)
