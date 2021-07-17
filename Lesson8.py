# symbols = {symbol: ord(symbol) for symbol in 'qwerty'}
# print(symbols)
#
# persons = {'John': 12, 'Jack': 34, 'Anna': 27}
# print(persons)
#
# persons['Jay'] = 59
# persons['John'] = 73
# print(persons)
#
# result = 'Anna' in persons
# print(result)
#
# key = 'Anna'
# if key not in persons:
#     persons[key] = 41
#
# for key in persons:
#     print(key, persons[key])
#
# for item in persons.items():
#     print(item)
#
# persons = {'John': 12, 'Jack': 34}
# persons_other = {'Anna': 42, 'Jack': 44}
# persons.update(persons_other)
# print(persons)

products = [{'name': 'water', 'price': 12, 'title': 'Bonaqua'},
            {'name': 'bread', 'price': 7, 'title': 'Baton'},
            {'name': 'bread', 'price': 9, 'title': 'WhiteBread'},
            {'name': 'apple', 'price': 25, 'title': 'Golden'}]

# for product in products:
#     product['sale'] = True
# print(products)

for product in products:
    if product['name'] == 'bread':
        product['price'] *= 2
