
initial_distance = int(input("Enter the start day distance: "))
finishing_distance = int(input("Enter the finish distance: "))
middle_result = initial_distance
day = 0

while middle_result < finishing_distance:
    middle_result = middle_result * 1.10
    day = day + 1
    print(middle_result)
print(f'"The sportsman achieved the finishing distance at day:" {day}')
