
def my_func():
    """создаем две переменных для ввода слогаемых сумм"""
    list_numbers_1 = sum(list(map(int, input("Введите несколько цифр через пробел: ").split())))
    print(list_numbers_1)
    list_numbers_2 = sum(list(map(int, input("Введите несколько цифр через пробел: ").split())))
    return list_numbers_2 + list_numbers_1


print(my_func())


