# count = 10
# while count > 0:
#     count -= 1
#     print(f'count = {count}')
# print('The end')

tmp_value = 5
go_game = True
while go_game:
    value = input('введите число от 1 до 10: ')
    if str(tmp_value) == value:
        go_game = False
        print('Угадал')
    elif str(tmp_value) > value:
        print('Попробуй больше')
    elif str(tmp_value) < value:
        print('Попробуй меньше')

# ДЗ* Давать подсказки типа: Попробуй больше или именьше