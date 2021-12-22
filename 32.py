#program 3 validasi tanggal dengan format dd mm yyyy
time = input().split()

tanggal = int(time[0]) 
bulan = int(time[1]) 
tahun = int(time[2])

if (bulan == 1 or bulan == 3 or bulan == 5 or bulan == 7 or bulan == 8 or bulan == 10 or bulan == 12) and tanggal <=31:
    print("valid")
elif (bulan == 4 or bulan == 6 or bulan == 9 or bulan == 11) and tanggal <= 30:
    print("valid")
elif bulan == 2:
    if tahun % 400 == 0 or (tahun % 4 == 0 and not tahun % 100 == 0):
        if tanggal <= 29:
            print("valid")
        elif tanggal > 29:
            print("tidak valid")
    else:
        if tanggal <= 28:
            print("valid")
        else:
            print("tidak valid")
else:
    print("tidak valid")

#bila diinputkan = 31 4 2019
#output = tidak valid
