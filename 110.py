#katanya ditest

n=7

for i in range(1, n+1):
    for j in range(1, n + 4):
        if i == j:
            print(j, end="")
        elif j == i + 1:
            print("*", end="")
        elif j == i + 2:
            print("*", end="")
        else:
            print(j, end="")
    print()
