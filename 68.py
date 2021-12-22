intvawal = int(input()) #input
intvakhir = int(input()) #input

intvakhirfix = intvakhir + 1 #menentukan interval akhir agar inklusif

las = [] #list kosong untuk menampung primary numbers

for i in range(intvawal, intvakhirfix): #looping for untuk setiap angka inklusif pada interval yang sudah ditentukan
    if i > 1: #kondisi ketika elemen angka dalam interval lebih besar dari 1 karena dibawah 1 pasti bukan prima 
        for j in range(2, i): #looping for dalam for untuk menemukan angka yang bukan prima karena akan habis bila dibagi
            if i%j == 0: #kondisional untuk mendeteksi angka bukan prima karena angka dibagi range antara 2 - i yaitu misal i = 5 maka range( 2,5) = 2-4 karena tidak ada sisa bagi 0 maka program akan ke else 
                break #bila angka bukan prima maka for aka break dan ke for awal 
        else:
            las.append(i) #masukkan angka prima ke list kosong las dengan append method

for numprime in las: #lakukan perulangan pada list las untuk output angka prima pada interval
    print(numprime)



