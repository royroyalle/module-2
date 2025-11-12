print("Welcome to age checker of this Class")
age = int(input("Please enter our age:"))
if age >= 9.9 and age <= 19.9:
    print("Welcome")
    if age >= 14 and age <= 16.9:
        print("Senior Status")
    if age >= 17 and age <= 19.9:
        print("Veteran Status")
else:
    print("You are restricted")