row = int(input("Enter the number of the row : "))

for i in range(row):
    for j in range(i + 1):
        print("* ", end="")
    print()