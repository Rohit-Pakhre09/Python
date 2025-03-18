num = int(input("Enter any number: "))

length = len(str(num))
temp = num
answer = 0

while temp > 0:
    remainder = temp % 10
    answer += remainder**length
    temp = temp // 10

if num == answer:
    print(f"{num} is an Armstrong Number.")
else:
    print(f"{num} is not an Armstrong Number.")