num = int(input("Enter the number to generate its Multiplication Table : "))

for i in range(1, 11):
    ans = num * i
    print(f"{num} x {i} = {ans}")