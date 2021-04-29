
random_list = []
element_count = int(input("Enter the total number of elements: "))
while element_count > 0:
    random_list.append(input("Enter elements into the list to see magic: "))
    element_count -= 1

for i in range(0, len(random_list) - 1, 2):
    random_list[i], random_list[i+1] = random_list[i+1], random_list[i]
print(random_list)
