my_list = [1, 2, 3, 4, 5, 6]
new_list = my_list.copy()[1:]
new_list.append(my_list[0])

print(new_list)