num = int(input("Enter any number : "))
reversed_num = 0
temp = num

while num != 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num //= 10

print(f"Reversed Number of {temp}: {reversed_num}")