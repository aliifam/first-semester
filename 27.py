#aplikasi angka terbilang

numbers = input("masukkan angka: ")

terjemahan = {
    "0" : "nol",
    "1" : "satu",
    "2" : "dua",
    "3" : "tiga",
    "4" : "empat",
    "5" : "lima",
    "6" : "enam",
    "7" : "tujuh",
    "8" : "delapan",
    "9" : "sembilan",
}

output = ""

for n in numbers:
    terbilang = terjemahan.get(n, "invalid")
    
    output = output + terbilang + " "
    
print(output)

