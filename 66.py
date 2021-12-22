#nearest prime nnumber
angka = int(input())

lst = []

for i in range(2, angka):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime == True:
        lst.append(i)

lstprime = []
for i in lst:
    if angka>i and angka-i>0:
        lstprime.append(i)
print(lstprime[-1])

