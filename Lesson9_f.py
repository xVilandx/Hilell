import random


def create_point(min_limit, max_limit):
    point = {'x': random.randint(min_limit, max_limit),
             'y': random.randint(min_limit, max_limit)}
    return point


def create_triangle(point_name, min_limit, max_limit):
    return {key: create_point(min_limit, max_limit) for key in point_name}


triangle_ABC = create_triangle('ABC', -150, 100)

print(triangle_ABC)