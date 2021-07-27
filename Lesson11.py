import json


def write_json(file_name, data):
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file)


def read_json(file_name):
    with open(file_name, 'r') as json_file:
        data = json.load(json_file)
        return data


data_list = [1, 2, 3, 4, 5]
data_dict = {'name': 'John',
             'age': 13,
             'job': {'title': 'Dev ops',
                     'price': '1000$'}}

# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file)

# with open('data.json', 'r') as json_file:
#     new_data = json.load(json_file)

filename = 'data_list.json'
write_json(filename, data_list)
read_json(filename)
