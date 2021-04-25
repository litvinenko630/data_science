
my_list = [7, 5, 3, 3, 3, 2]
my_number = int(input("Введите любое натуральное число: "))

if my_number in my_list:
    position_index = my_list.index(my_number) + my_list.count(my_number)
    my_list.insert(position_index, my_number)
    print(my_list)
else:
    my_list.append(my_number)
    print(sorted(my_list, reverse=True))