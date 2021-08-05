import json


def read_file(file_json):
    with open(file_json, 'r') as json_file:
        return json.load(json_file)


def sort_by_surname(list_authors):
    surname = list_authors['name']
    if len(surname) > 1:
        surname = surname.split(' ')
        surname = surname[len(surname)-1]
    return surname


def sort_by_death(list_authors):
    my_date = [int(value) for value in list_authors['years'].strip('.').split() if value.isdigit()]
    return -min(my_date) if 'BC' in list_authors['years'] else max(my_date)


def sort_by_len_text(list_authors):
    return len([my_str for my_str in list_authors['text'].split()])


# 1 task
date_json = read_file('data.json')

# 2 task
sorted_date_surname = sorted(date_json, key=sort_by_surname)

# 3 task
sorted_date_death = sorted(date_json, key=sort_by_death)

# 4 task
sorted_date_len_text = sorted(date_json, key=sort_by_len_text)
