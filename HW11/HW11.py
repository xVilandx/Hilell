import json


def read_file(file_name):
    with open(file_name, 'r') as json_file:
        return json.load(json_file)


def sort_by_surname(file_name):
    surname = file_name['name']
    if len(surname) > 1:
        surname = surname.split(' ')
        surname = surname[len(surname)-1]
    return surname


def sort_by_date(file_name):
    my_date = [int(value) for value in file_name['years'].strip('.').split() if value.isdigit()]
    return -min(my_date) if 'BC' in file_name['years'] else max(my_date)


def sort_by_len_text(file_name):
    return len([my_str for my_str in file_name['text'].split()])
