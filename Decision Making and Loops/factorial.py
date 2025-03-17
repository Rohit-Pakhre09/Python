num = int(input("Enter any number : "))
fact = 1

if num <= 0:
    print("Factorial does not exist for the negative number.")
else:
    for i in range(1, num + 1):
        fact *= i

print(f"The factorial of the {num} is the {fact}")