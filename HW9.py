import random as rnd
import string


def do_task_1(name_list):
    return [symbol[::-1] if not index % 2 else symbol for index, symbol in enumerate(name_list)]


def do_task_2(name_list):
    return [symbol for symbol in name_list if symbol[0].find('a') >= 0]


def do_task_3(name_list):
    return [symbol for symbol in name_list if symbol.find('a') >= 0]


def do_task_4(name_list):
    return [my_str for my_str in name_list if isinstance(my_str, str)]


def do_task_5(name_str):
    return [symbol for symbol in set(name_str) if my_str.count(symbol) == 1]


def do_task_6(name_str_1, name_str_2):
    return list(set(name_str_1).intersection(name_str_2))


def do_task_7(str_1, str_2):
    return [symbol for symbol in set(str_1 + str_2) if str_1.count(symbol) == 1 and str_2.count(symbol) == 1]


def do_task_8(list_name, domains_name):
    letter = ''.join(rnd.choice(string.ascii_letters) for count in range(0, rnd.randint(5, 7)))
    return rnd.choice(list_name) + '.' + str(rnd.randint(100, 999)) + '@' + letter + '.' + rnd.choice(domains_name)


# 1
my_list = ['hello', 'beautiful', 'world', 'goodbye', 'boring', 'job']
new_list = do_task_1(my_list)

###################################

# 2
my_list = ['add', 'advance', 'good', 'monday', 'toy', 'new', 'create', 'boy']
new_list = do_task_2(my_list)

###################################

# 3
my_list = ['add', 'advance', 'good', 'monday', 'toy', 'new', 'create', 'boy']
new_list = do_task_3(my_list)

###################################

# 4
my_list = [1, '2', 3, '4', 5, '6', 7, '8']
new_list = do_task_4(my_list)

###################################

# 5
my_str = 'Hello world'
my_list = do_task_5(my_str)

###################################

# 6
my_str_1 = 'qwerty'
my_str_2 = 'rtyuio'

new_list = do_task_6(my_str_1, my_str_2)

###################################

# 7
my_str_1 = 'Иван Петрович'
my_str_2 = 'Владимир Александрович'
my_list = do_task_7(my_str_1, my_str_2)

###################################

# 8
names = ['wild', 'crazy', 'smash', 'custom', 'ghost']
domains = ['com', 'net', 'ua', 'ru', 'biz']
e_mail = do_task_8(names, domains)
print(e_mail)
