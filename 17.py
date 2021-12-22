#game tebak angka 4 jam wkwkwk

percobaan = 0
jawaban = 8 
batas_mencoba = 3

while percobaan < batas_mencoba:
    angka_dicoba = input("masukkan angka (1-9) : ")
    angka_dicoba = int(angka_dicoba)
    
    if angka_dicoba == jawaban:
        print("selamat tebakan anda benar")
        break
    
    percobaan +=1
