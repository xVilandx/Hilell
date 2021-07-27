test_str = 'qwerty!@#$%^asfewfdsdstesgd . 21@3$t435'
result =[]
for symbol in test_str:
    if symbol.lower() not in 'etuioa' and symbol.isalpha():
        #print(f'symbol = {symbol}')
        result.append(symbol)
print(result)

join_str = '_'.join(result)
print(join_str)

# split_str = list(test_str)
# print((split_str))

# tuple - кортеж - не изменяемый тип
# list - список - изменяемый тип

# my_tuple = (1, 2, 'qwe', (-1, 0), None)
# print(type(my_tuple), my_tuple)
#
# my_list = [1, 2, 'qwe', (-1, 0), None]
# print(type(my_list), my_list)
#
# index = 0
# my_list[index] = 3
#
# value_tuple = my_tuple[index]
# value_list = my_list[index]
#
# print(value_tuple, value_list)

# приведение к типам
# new_list = list(my_tuple)
# new_tuple = tuple(my_list)
# print(type(new_list), new_list)
# print(type(new_tuple), new_tuple)

# new_list = []
# new_list.append('first')
# new_list.append('second')
# new_list.append([1, 3, 5])
# last_value = new_list.pop()
# print(new_list)