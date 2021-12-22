#zebra cross

n = int(input())
m = input()

lst = []

if m == "H":
    for i in range(n):
        if (i%2) == 0:
            print("#"*n)
        elif (i%2) == 1:
            print("-"*n)
elif m == "V":
    for i in range(n):
        if (i%2) == 0:
            lst.append("#")
        elif (i%2) == 1:
            lst.append("|")
    zcv = ''.join(lst)
    for i in range(n):
        print(zcv)
