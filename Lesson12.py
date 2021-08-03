# my_list = [4, 6, 1, 2, 35, 12, 65, -5, -1, 0]
# sorted_list = sorted(my_list, reverse=True)
# print(sorted_list)
#
#
# def sort_by_len_and_name(name):
#     return len(name), name
#
#
# my_str_list = ['Anna', 'Jack', 'Jonny', 'Andrey', 'Vita']
# sort_str_list = sorted(my_str_list, key=len)
# print(sort_str_list)
#
# sort_str_list = sorted(my_str_list, key=sort_by_len_and_name)
# print(sort_str_list)
#
# def sort_by_price(price_dict):
#     price = price_dict['price']
#     name = price_dict['product']
#     return price, name
#
#
# price_list = [{'product': 'milk', 'price': 23},
#               {'product': 'ice-cream', 'price': 18},
#               {'product': 'meat', 'price': 120},
#               {'product': 'Coca-Cola', 'price': 10},
#               {'product': 'Pepsi-Cola', 'price': 10}]
# sorted_price_list = sorted(price_list, key=sort_by_price)
# print(sorted_price_list)
#
import re

my_string = 'adasfekfnadjf3295824058023581032naefeoa, asw 168.0.0.1 asdqeqhg;ksdpvp zfwqofmfaosc yy 200.23.12.201:5400 '
template = r'\d+'
template_2 = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

result = re.findall(template_2, my_string)
print(result)