str = input("Enter a word")
chr = input("Enter a character")

i = 0
count = 0
while (i < len(str)):
    if (str[i] == chr):
        count = count + 1
    i = i + 1
print("Total number of times", chr, "has repeated in", str, "is...", count)
