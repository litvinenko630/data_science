
def my_func():
    """создаем две переменных для делимого и делителя"""
    first_number = int(input("Введите любое число : "))
    second_number = int(input(f"На каоке число вы хотите поделить число {first_number}: "))
    if second_number == 0:
        while second_number == 0:
            second_number = int(input(f"Введите любле число отличное от 0: "))
        return first_number / second_number
    else:
        return first_number/second_number


print(my_func())
