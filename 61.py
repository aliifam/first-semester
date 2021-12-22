angka = input().split()

lsta = [int(a) for a in angka]
angka.remove(max(angka))
print(max(angka))
