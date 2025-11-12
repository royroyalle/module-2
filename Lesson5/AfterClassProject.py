print("Welcome to decimal to binar number calculator")
decimal = int(input("Please enter a non negative number "))
temp = decimal
binary = ""
while temp > 0:
         rem = temp % 2
         binary = str(rem) + binary
         temp = temp // 2
print("binary version:", binary)
