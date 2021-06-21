# 1 задание
my_list = [150, 100, 50, 60, 46, 967, 464, 1, 77, 345]
for index in my_list:
    if index > 100:
        print(index)

#######################################################

# 2 задание
my_list = [150, 100, 50, 60, 46, 967, 464, 1, 77, 345]
my_result = []
for index in my_list:
    if index > 100:
        my_result.append(index)

print(my_result)

#######################################################

# 3 задание
my_list = [50, 150, 100]
if len(my_list) < 2:
    my_list.append(0)
else:
    my_list.append(my_list[len(my_list) - 1] + my_list[len(my_list) - 2])

#######################################################

# 4 задание
value = input('Введите число с точкой: ')

try:
    print(float(value) ** -1)
except ValueError:
    print('Кто-то ввел не цифру с точкой')
except ZeroDivisionError:
    print('Ноль не подходит)')

#######################################################

# 5 задание
my_string = '0123456789'
my_list = []
for symbol_1 in my_string:
    for symbol_2 in my_string:
        my_number = symbol_1 + symbol_2
        my_list.append(int(my_number))

print(my_list)