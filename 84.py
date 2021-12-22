#bounce ball
import math
masuk = input().split()

n = int(masuk[0])
a = int(masuk[1])
b = int(masuk[2])

t = n*100 #konversi ukuran

lting = []

awal = 1

while 1<=awal<t:
    grow = t*(a/b)**awal
    awal+=1 
    if grow < 1:
        break
    lting.append(grow)

total = (math.ceil(sum(lting))*2 + t)   

print(total)
