
def my_func(x, y):
    """возводим позиционные аргументы в степень Решение 1"""
    my_number = x**y
    return my_number


print(my_func(2, -5))


def my_func(x, y):
    """возводим позиционные аргументы в степень Решение 2"""
    my_number = 1
    for i in range(abs(y)):
        my_number = my_number * x

    return 1 / my_number


print(my_func(2, -5))
