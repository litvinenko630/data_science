user_number = abs(int(input("Enter any number:")))
max_number = 0

while user_number > 0:
    item = user_number % 10
    print(item)
    if item >= max_number:
        max_number = item

    user_number = user_number // 10

print(max_number)

