import random

# value = random.randint(10, 20)
# my_list = [1, 2, 5, 10, 15, 50]
# choice_from_list = random.choice(my_list)
# print(value, choice_from_list)

point_M = {'x': random.randint(-10, 10),
           'y': random.randint(-10, 10)}

point_N = {'x': random.randint(-10, 10),
           'y': random.randint(-10, 10)}

point_K = {'x': random.randint(-10, 10),
           'y': random.randint(-10, 10)}

triangle_MNK = {'M': point_M,
                'N': point_N,
                'K': point_K}
print(triangle_MNK)