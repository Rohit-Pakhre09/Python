num = int(input("Enter any number : "))

a, b = 0, 1
c = a + b
print("Fibonacci Series :-")
print(a, end=", ")
print(b, end=", ")

for i in range(3, num + 1):
    print(c, end=", ")
    a = b
    b = c
    c = a + b