#program harga sepatu dan baju budi

#input bulan1
bulan1 = input().split()

sepatu1 = int(bulan1[0])
baju1 = int(bulan1[1])
tharga1 = int(bulan1[2])

#input bulan2
bulan2 = input().split()

sepatu2 = int(bulan2[0])
baju2 = int(bulan2[1])
tharga2 = int(bulan2[2])

#selesaikan dengan basic linear algebra 
wadezig = abs(tharga1 - tharga2)
hargabaju = abs(wadezig / (baju1 - baju2)) 

hargasepatu = abs((tharga1 - (baju1*hargabaju)) / sepatu1)



print(int(hargasepatu), int(hargabaju))
# 224500 21300