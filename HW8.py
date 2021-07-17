# 1 task
list_persons = [{'name': 'John', 'age': 25},
                {'name': 'Anna', 'age': 20},
                {'name': 'Eva', 'age': 19},
                {'name': 'Masha', 'age': 34},
                {'name': 'Anton', 'age': 19}]

age_persons = [person['age'] for person in list_persons]    # список всех возрастов
young_persons = [person['name'] for person in list_persons if person['age'] == min(age_persons)]    # самые молодые

len_name_persons = [len(person['name']) for person in list_persons]  # длина имен
longest_name_persons = [person['name'] for person in list_persons if len(person['name']) == max(len_name_persons)]    # самые длинные имена

average_age = sum(age_persons) / len(age_persons)    # среднее количество лет

# 2 task

my_dict_1 = {1: 10, 3: 45, 5: 20, 9: 140}
my_dict_2 = {2: 15, 3: 56, 6: 20, 9: 140}

list_intersection_dict_1_2 = list(set(my_dict_1).intersection(my_dict_2))    # общие ключи

list_difference_dict_1_2 = list(set(my_dict_1).difference(my_dict_2))    # уникальные ключи из первого словаря

new_dict = {keys: my_dict_1[keys] for keys in list_difference_dict_1_2}    # словарь из пар с уникальными ключами

list_unique_keys = list(set(my_dict_1).symmetric_difference(my_dict_2))
new_dict_2 = {keys: (my_dict_1 | my_dict_2)[keys] for keys in list_unique_keys}
new_dict_2.update({key: [my_dict_1[key], my_dict_2[key]] for key in list_intersection_dict_1_2})  # объедененные словари
