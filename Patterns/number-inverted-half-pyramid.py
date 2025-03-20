row = int(input("Enter the number of the row : "))

for i in range(row, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()