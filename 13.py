#persamaan kuadrat
psk = input().split()

a = int(psk[0])
b = int(psk[1])
c = int(psk[2])

#process with formula
d = b**2 - 4*a*c
y = -(d) / (4*a)

#max y
print(int(y))

