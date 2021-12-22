#tebak tinggi 

lstsize = []

jum = int(input())

for i in range(jum):
    ting = int(input())
    lstsize.append(ting)

lstsize.sort()

adi = lstsize.index(165)

print(adi + 1)
