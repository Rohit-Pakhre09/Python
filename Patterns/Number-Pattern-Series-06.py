# 5
# 4 4
# 3 3 3
# 2 2 2 2
# 1 1 1 1 1

for i in range(5, 0, -1):
    for j in range(6 - i):
        print(i, end=" ")
    print()