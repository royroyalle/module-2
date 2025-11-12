print("Welcome to Digit checker")
num = int(input("Enter your number")) 
temp = num
digit = 0
if temp == 0:
    digit = 1
else:
    while temp > 0:
        temp = temp // 10
        digit = digit + 1
print("The number of digits is:", digit)