#no a 
duit = input().split(" ")

a = int(duit[0])
b = int(duit[1])
c = int(duit[2])
d = int(duit[3])

untung1 = b - a 

untung2 = d - c

totaluntung = untung1 + untung2

totalrugi = abs(totaluntung)

if totaluntung > 0:
    print(totaluntung)
elif totaluntung == 0:
    print("impas")
else:
    print('-' + str(totalrugi))

