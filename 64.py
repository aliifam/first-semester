#M besar mana sih?

angka = input().split()

a = float(angka[0])
b = float(angka[1])
c = float(angka[2])
d = float(angka[3])

tot1 = a / b 
tot2 = c / d 

if tot1>tot2:
    print(">")
elif tot1<tot2:
    print("<")
elif tot1 == tot2:
    print("=")
