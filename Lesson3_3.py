
def my_func(a, b, c):
    """создаем список позиционных аргументов, удаляем наименьшее из них, вызываем сумму"""
    max_number = [a, b, c]
    max_number.remove(min(max_number))
    return sum(max_number)


print(my_func(31000, 891736, 31000,))
