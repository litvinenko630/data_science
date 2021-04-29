
my_string = input("Введите несколько слов через пробел: ").split()
for ind, el in enumerate(my_string):
    print(ind, el[:10])
