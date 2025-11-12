print("Half Pyramid Pattern of Stars (*):")
q = int(input("Enter Number of Rows:"))

for i in range(q):
    for j in range(i+1):
        print("*", end="")
    print()