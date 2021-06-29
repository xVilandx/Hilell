# 1
my_number = 6452341053015813000480130000
zero = 0
print(str(my_number).count(str(zero)))

###########################################

# 2
my_number = 4322530002510034250000000000
print(len(str(my_number)) - len(str(int(str(my_number)[::-1]))))

###########################################

# 3
my_list_1 = [1, 2, 3, 4, 5, 6]
my_list_2 = ['q', 'w', 'e', 'r', 't', 'y']
my_result = []

for index, symbol in enumerate(my_list_1):
     if not index % 2:
         my_result.append(symbol)

for index, symbol in enumerate(my_list_2):
     if index % 2:
         my_result.append(symbol)

###########################################

# 4
my_list = [1, 2, 3, 4, 5, 6]
new_list = my_list.copy()[1:]
new_list.append(my_list[0])

print(new_list)

##########################################

# 5
my_list = [1, 2, 3, 4, 5, 6]
my_list.append(my_list.pop(0))

###########################################

# 6
my_str = '55 можно разделить нацело на 11 но нельзя на 2'
new_my_list = my_str.split()
sum_number_my_str = 0

for number in new_my_list:
    if number.isdigit():
        sum_number_my_str += int(number)

print(sum_number_my_str)

###########################################

# 7
my_str = 'Это "как буд-то" ну ооооочень длииииинаааая строка'
l_symbol = 'н'
r_symbol = 'о'
print(my_str[my_str.find(l_symbol)+1:my_str.rfind(r_symbol)])

###########################################

# 8
my_str = 'qwertyu'
my_list = []
my_number = 0
while my_number < len(my_str):
    if len(my_str) % 2 and my_number == len(my_str)-1:
        my_list.append(my_str[my_number] + '_')
        my_number += 2
    else:
        my_list.append(my_str[my_number:my_number + 2])
        my_number += 2

###########################################

# 9
my_list = [1, 5, 3, 9, 5, 4, 6, 9, 2, 0, 5, 7, 1]
happy_numbers = 0
for index in range(len(my_list)):
    if my_list[index] > my_list[index-1] + my_list[(index+1) % len(my_list)]:
        happy_numbers += 1

print(happy_numbers)