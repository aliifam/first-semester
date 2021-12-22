#input 4 digit of interger and this program will split the digit and count it

angka = int(input())

digit1 = int(angka / 1000)
digit2 = int(angka % 1000 / 100)
digit3 = int(angka % 1000 % 100 / 10)
digit4 = int(angka % 1000 % 100 % 10)

total = digit1 + digit4 + digit2 + digit3

print(total)