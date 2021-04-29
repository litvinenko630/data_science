
def int_func(letter):
    """создаем переменную для помещения значения"""
    word = letter.title()
    return word


print(int_func(input("Enter some words in lowercase spaced by one: ")))