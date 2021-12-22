#no 1 dan 2

u1 = int(100000)
u2 = int(50000)
u3 = int(10000)
u4 = int(5000)
u5 = int(1000)
u6 = int(500)
u7 = int(10)
u8 = int(5)
u9 = int(1)

uang = int(input())
totlem = []
sisa = uang

while sisa > 0:
    if sisa >= u1:
        banyak_lembar = int(sisa/u1)
        sisa = sisa - (u1*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 100.000 rupiah")
    elif sisa >= u2:
        banyak_lembar = int(sisa/u2)
        sisa = sisa - (u2*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 50.000 rupah")
    elif sisa >= u3:
        banyak_lembar = int(sisa/u3)
        sisa = sisa - (u3*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 10.000 rupah")
    elif sisa >= u4:
        banyak_lembar = int(sisa/u4)
        sisa = sisa - (u4*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 5000 rupah")
    elif sisa >= u5:
        banyak_lembar = int(sisa/u5)
        sisa = sisa - (u5*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 1000 rupah")
    elif sisa >= u6:
        banyak_lembar = int(sisa/u6)
        sisa = sisa - (u6*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 500 rupah")
    elif sisa >= u7:
        banyak_lembar = int(sisa/u7)
        sisa = sisa - (u7*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 10 rupah")
    elif sisa >= u8:
        banyak_lembar = int(sisa/u8)
        sisa = sisa - (u8*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 5 rupah")
    elif sisa >= u9:
        banyak_lembar = int(sisa/u9)
        sisa = sisa - (u9*banyak_lembar)
        totlem.append(banyak_lembar)
        print(banyak_lembar, "lembar 1 rupah")
print("total",sum(totlem),"Lembar uang kertas")
    
    
