#solving soal UAS ADP nomor 2

masukan = input().split(" ")

n = int(masukan[0]) #jumlah mahasiswa

k = int(masukan[1]) #jumlah kelompok yang mau dibuat

if n%k == 0:
    hasil = n/k
    while n > 0:
        n-=hasil
        print(int(hasil), end=" ")
else:
    hasil = int(n/k)
    temp = []
    jm = n
    while n > hasil:
        n-=hasil
        temp.append(hasil)
    peng = jm - sum(temp)
    rata = 1
    g = -1
    while peng > 0:
        temp[g] += 1
        peng-=1
        g = g - 1
    for i in temp:
        print(i, end=" ")

#misal diinput 20 6 maka output = 3 3 3 3 4 4 
#misal diinput 10 2 maka output = 5 5 
