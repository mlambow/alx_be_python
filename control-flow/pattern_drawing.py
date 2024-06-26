length = int(input("Enter the size of the pattern: "))
size = 0

while size < length:
    for i in range(length):
        print("*", end="")
    print()
    size +=1
print()