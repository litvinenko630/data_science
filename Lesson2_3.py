
month_index = int(input("Enter the number of the month to know the time of the year: "))
year_dict = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June",
             7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

if 1 <= month_index < 3:
    print(f"You entered {year_dict.get(month_index)} which is one of the Winter months")
elif 3 <= month_index < 6:
    print(f"You entered {year_dict.get(month_index)} which is one of the Spring months")
elif 6 <= month_index < 9:
    print(f"You entered {year_dict.get(month_index)} which is one of the Summer months")
elif 9 <= month_index < 12:
    print(f"You entered {year_dict.get(month_index)} which is one of the Fall months")


