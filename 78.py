nama = input().split(" ")

lnama = []

for i in nama:
    lnama += [i]
    
print(min(lnama, key=len))

