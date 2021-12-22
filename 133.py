angka = int(input())

digit1 = int(angka / 100)
digit2 = int((angka % 100) / 10)
digit3 = int(angka % 100 % 10)

total = digit1 + digit2 + digit3

print(total)

