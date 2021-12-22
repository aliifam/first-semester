#pembagian helm
#bensin
tbensin = int(input())

motor = input().split(" ")

mobil = input().split(" ")

mot = []
mob = []

for i in motor:
    i = int(i)
    mot.append(i)

for j in mobil:
    j = int(j)
    mob.append(j)

sisa = tbensin

motisi = []
mobisi = []

for k in range(len(mot)):
    if sisa > 0:
        sisa = sisa - mot[k]
        motisi.append(k)

if len(motisi) > 0:
    print(len(motisi))
else:
    print(0)

for m in range(len(mob)):
    if sisa > 0:
        sisa = sisa - mob[m]
        mobisi.append(m)
        
if len(mobisi) > 0:
    print(len(mobisi))
else:
    print(0)
    


