#exception handling

try:
    angka = int(input())
    operasi = angka / 0
    print(operasi)
except:
    print('terjadi kesalahan')
