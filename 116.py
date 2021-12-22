n = int(input())
koor = input().split()

x = int(koor[0])
y = int(koor[1])

for i in range(n):
    for j in range(n):
        if j == x - 1 and i == y - 1:
            print("X", end="")
        else:
            print("*", end="")
    print()
