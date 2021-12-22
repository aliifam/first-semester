#ppkuasno7

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())

tj = 10000

th = 0

lh = [a, b, c, d, e, f, g]

lend = []

while th < tj:
    for i in lh:
        if tj > 0:
            tj = tj - i
            lend.append(i)
        else:
            break

print(len(lend))
