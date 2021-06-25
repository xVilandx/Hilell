# my_list = [1, 2, 3]
# new_list = [my_list] * 3
# print(new_list)
# my_list.append(4)
# print(my_list)
# print((new_list))

# 1
# my_str = 'blablacar'
# my_symbol = 'bla'
#
# result = my_str.count(my_symbol)
# print(result)

# 2
# my_str = 'blablacar'
# my_symbol = 'bla'
#
# my_symbol_count = my_str.count(my_symbol)
# for index in range(my_symbol_count):
#     print(my_symbol)

# 3
# my_str = 'bla BLA car'
# my_str = my_str.lower()
# symbols_heap = []
# for symbol in my_str:
#     if symbol not in symbols_heap:
#         symbols_heap.append(symbol)
# res_len = len(symbols_heap)
# print(res_len)
# print(symbols_heap)

# 4
# my_str = 'qwerty'
# my_list = []
# for index in range(len(my_str)):
#     if not index % 2:
#         symbol = my_str[index]
#         my_list.append(symbol)
#
# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
#
# print(my_list)

# 5
# my_str = 'qwerty'
# my_list = []
# str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]
#
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)

# 6
# my_number = 243959204579024594375802374851305942759
# digit_count = len(str(my_number))
# print(digit_count)

# 7
# my_number = 243520457024543758023748513054275
# number_str = str(my_number)
# max_symbol = max(number_str)
# print(max_symbol)

# 8
# my_number = 243959204579024594375802374851305942759
# number_str = str(my_number)
# new_number_str = number_str[::-1]
# new_number = int(new_number_str)
# print(new_number_str)

# 9
# my_list = [1, 2, 5, 3, -8, 4]
# my_str = 'qwerty'
# sorted_list = sorted(my_str, reverse=True)
# print(sorted_list)

# my_number = 243959204579024594375802374851305942759
# number_str = str(my_number)
# sorted_number_symbols_list = sorted(number_str)
# new_number_str = ''.join(sorted_number_symbols_list)
# new_number = int(new_number_str)
# print(new_number)

# new_number = int(''.join(sorted(str(my_number))))
# print(new_number)