num = int(input("Enter any number : "))
is_prime = True

if num == 0 or num == 1:
    print(f"{num} is not a Prime number.")
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is the Prime number.")
else:
    print(f"{num} is not the Prime number.")