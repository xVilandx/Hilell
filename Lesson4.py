# value = input('Введите целое число: ')
# if value.isdigit():
#     value = int(value)
#     result = value * 2
#     print(result)
# else:
#     print('Вы ввели не целое число')
#
# try:
#     value = float(value)
#     result = 1 / value
#     print(result)
# except (ValueError, ZeroDivisionError):
#     print('Попробуй еще')
#     result = 0
# except ValueError:
#     print('Число не может быть приведено к типу float')
#     result = 0
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
#     result = -1
#
# print(result)