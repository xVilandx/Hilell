value = int(input('Введите число: '))
new_value = value / 2 if value < 100 else -value
print(new_value)

#######################################

# 2 задание
value = int(input('Введите число: '))
new_value = 1 if value < 100 else 0
print(new_value)

#######################################

# 3 задание
value = int(input('Введите число: '))
new_value = True if value < 100 else False
print(new_value)

#######################################

# 4 задание
my_str = input('Введите строку: ')
my_str = my_str.upper()
print(my_str)

#######################################

# 5 задание
my_str = input('Введите строку: ')
my_str = my_str.lower()
print(my_str)

#######################################

# 6 задание
my_str = input('Введите строку: ')
my_str = my_str + my_str if len(my_str) < 5 else my_str
print(my_str)

#######################################

# 7 задание
my_str = input('Введите строку: ')
my_str = my_str + my_str[::-1] if len(my_str) < 5 else my_str
print(my_str)