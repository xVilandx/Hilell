# 1
my_list = ['hello', 'beautiful', 'world', 'goodbye', 'boring', 'job']
new_list = []

for index, symbol in enumerate(my_list):
    if not index % 2:
        new_list.append(symbol[::-1])
    else:
        new_list.append(symbol)

print(new_list)

###################################

# 2
my_list = ['add', 'advance', 'good', 'monday', 'toy', 'new', 'create', 'boy']

new_list = [symbol for symbol in my_list if symbol[0].find('a') >= 0]

print(new_list)

###################################

# 3
my_list = ['add', 'advance', 'good', 'monday', 'toy', 'new', 'create', 'boy']

new_list = [symbol for symbol in my_list if symbol.find('a') >= 0]

print(new_list)

###################################

# 4
my_list = [1, '2', 3, '4', 5, '6', 7, '8']

new_list = [my_str for my_str in my_list if isinstance(my_str, str)]

print(new_list)

###################################

# 5
my_str = 'Hello world'

my_list = [symbol for symbol in set(my_str) if my_str.count(symbol) == 1]

print(my_list)
###################################

# 6
my_str_1 = 'qwerty'
my_str_2 = 'rtyuio'

new_list = list(set(my_str_1).intersection(my_str_2))

print(new_list)

###################################

# 7
my_str_1 = 'Иван Петрович'
my_str_2 = 'Владимир Александрович'

my_list = [symbol for symbol in set(my_str_1+my_str_2) if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1]

print(my_list)
###################################

# 8
my_dict = {'surname': 'Ivanov',
           'name': 'Ivan',
           'age': 18,
           'residence': {'state': 'Ukraine',
                         'city': 'Kiev',
                         'street': 'Bankova street'},
           'job': {'Availability': '+',
                   'position': 'cashier'}}

###################################

# 9
my_dict = {'Составляющие': {'коржи': {'мука': '500 гр',
                                      'молоко': '200 гр',
                                      'масло': '100 гр',
                                      'Яйцо': '150 гр'},
                            'крем': {'сахар': '100 гр',
                                     'масло': '100 гр',
                                     'ваниль': '20 гр',
                                     'сметана': '50 гр'},
                            'глазурь': {'какао': '50 гр',
                                        'сахар': '100 гр',
                                        'масло': '120 гр'}}}
