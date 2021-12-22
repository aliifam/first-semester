#dp io jjjj

nama = input().split(" ")

lnama = list(nama)

total = []

for j in lnama:
    awal = 0
    for k in j:
        if (k == "i") or (k == "o"):
            awal+=1
    total.append(awal)

patokan = 0 
for t in range(len(lnama)):
    if total[t] > patokan:
        patokan = total[t]
        namafix = lnama[t]

print(namafix)


    

