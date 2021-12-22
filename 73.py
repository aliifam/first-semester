#katak
n = input().split(" ")

m = int(n[0])
cm = int(n[1])

jarak = m*100

js = jarak 

lompat = 0

while js > 0:
    jarak = jarak / 2
    js = js - jarak
    lompat = lompat + 1
    if js - cm <= 0:
        print(lompat)
        break
else:
    print(0)
    

