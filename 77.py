tanggal = input().split()
bulan1 = [1, 3, 5, 7,8,10,12]
bulan2 = [4,6,9,11]
bulan3 = [2]
for i in range(len(tanggal)):
    tanggal[i] = int(tanggal[i])
tanggal[0]+=35
for i in range(2):
    if tanggal[1] in bulan1:
        if tanggal[0] > 31:
            tanggal[0] -= 31
            tanggal[1] += 1
    if tanggal[1] in bulan2:
        if tanggal[0] > 30:
            tanggal[0] -= 30
            tanggal[1] += 1
    if tanggal[1] in bulan3:
        if tanggal[2]%400 == 0:
            if tanggal[0] > 29:
                tanggal[0] -= 29
                tanggal[1] += 1
        else:
            if tanggal[2] % 100 == 0:
                if tanggal[0] > 28:
                    tanggal[0] -= 28
                    tanggal[1] += 1
            elif tanggal[2]%4 == 0:
                if tanggal[0] > 29:
                    tanggal[0] -= 29
                    tanggal[1] += 1
            else:
                if tanggal[0] > 28:
                    tanggal[0] -= 28
                    tanggal[1] += 1
    if tanggal[1] > 12:
        tanggal[1] -= 12
        tanggal[2] += 1
baru = list(map(str, tanggal))
hasil = " ".join(baru)
print(hasil)
