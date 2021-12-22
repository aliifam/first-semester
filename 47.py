#swapping gen dna

baris1 = input()
baris2 = input()
baris3 = input()

j = "a" #define the string

lis1 = list(baris1)
lis2 = list(baris2)
lis3 = list(baris3)
lis4 = []

for i in range(0, len(lis3)):
    if lis3[i] == "1":
        lis4.append(lis2[i])
    elif lis3[i] == "0":
        lis4.append(lis1[i])

for i in range(0, len(lis4)):
    j = j+ lis4[i]
    
print(j[1:])


