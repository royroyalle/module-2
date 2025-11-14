
height = int(input("Enter number of rows:"))
for i in range(1, height + 1):
    space = height - i
    for j in range(space):
        print(" ", end="")
    a = i
    for k in range(a):
        print("*", end="")
    print()
q = height
for i in range(q):
    for j in range(i+1):
        print("*", end="")
    print()