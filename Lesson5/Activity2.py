up = int(input("Please enter your upper limit"))
low = int(input("Please enter your lower limit"))
for num in range(up, low + 1):
    if num > 1:
        for i in range (2, num):
            if (num % i) == 0:
                break
        else:
            print(num)