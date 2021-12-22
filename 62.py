#prima detected 

angka = int(input())

if angka > 1:
    for i in range(2, angka):
        if angka % i == 0:
            print("BUKAN")
            break
    else:
        print("PRIMA")
else:
    print("BUKAN")
