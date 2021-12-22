detik = int(input())
jam = detik / 3600
menit = detik % 3600 / 60
detik2 = detik %3600 % 60
print(int(jam))
print(int(menit))
print(int(detik2))