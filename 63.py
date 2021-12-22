import math
angka = float(input())

bulatkan = angka % round(angka)

if bulatkan >= 0.4:
    print(math.ceil(angka))
else:
    print(math.floor(angka))

