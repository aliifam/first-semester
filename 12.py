#program selisih dan konversi waktu
waktu1 = input().split()

jam1 = int(waktu1[0])
menit1 = int(waktu1[1])
detik1 = int(waktu1[2])

waktu2 = input().split()

jam2 = int(waktu2[0])
menit2 = int(waktu2[1])
detik2 = int(waktu2[2])

totaldetik1 = (jam1*60*60) + (menit1*60) + (detik1) #total detik 1
totaldetik2 = (jam2*60*60) + (menit2*60) + (detik2) #total detik 2

selisihdetik = totaldetik1 - totaldetik2

selisihjam = selisihdetik / 3600
selisihmenit = selisihdetik % 3600 / 60
selisihdetik2 = selisihdetik % 3600 % 60

print(int(selisihjam), int(selisihmenit), int(selisihdetik2))

