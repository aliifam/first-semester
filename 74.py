#aer 

air = int(input())

drigen = input().split(" ")

ldrigen = []

for i in drigen:
    i = int(i)
    ldrigen.append(i)

sisaair = air

ldrigenisi = []

for j in range(len(ldrigen)):
    if sisaair > 0:
        sisaair = sisaair - ldrigen[j]
        ldrigenisi.append(j)

if len(ldrigenisi) > 0:
    print(len(ldrigenisi))
else:
    print(0)
    
    


