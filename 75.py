#pengugsi e 
jp = int(input())

kr = input().split(" ")

kt = input().split(" ")

lkr = []
lkt = []

for i in kr:
    i = int(i)
    lkr.append(i)

for j in kt:
    j = int(j)
    lkt.append(j)
    
sisa = jp

mu = 0
peng = len(lkr)
jrp = []

while sisa > 0:
    sisa = sisa - lkr[mu]
    if sisa > 0:
        jrp.append(lkr[mu])
        mu += 1

print(len(jrp))

lai = 0
ngi = len(lkt)
jtp = []

while sisa > 0:
    sisa = sisa - lkt[lai]
    if sisa > 0:
        jtp.append(lkt[lai])
        lai += 1 
    
if len(jtp) > 0:
    print(len(jtp))
else:
    print(0)


    


