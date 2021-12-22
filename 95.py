#pr 3 adp rekursif
'''
f(5) = 5*(4/2)*3*(2/2)*1

f(7) = 7*(6/2)*5*(4/2)*3*(2/2)*1
'''
'''
PENJELASAN ALGORITMA REKURSIF
------------------------------
untuk menyelesaikan perhitungan diatas dengan mengimplementasikan fungsi rekursif saya membutuhkan satu basis
untuk kondisional agar tidak infinite looping dan memiliki dua kondisional rekurens yang pertama untuk angka
ganjil dan yang kedua untuk angka genap.

bila dibaca polanya maka bisa dilihat bila angka ganjil maka hanya akan dikalikan namun bila angka genap akan
dibagi 2 baru dikalikan dan bila sudah sampai angka 1 maka akan berhenti karena itu didapatkan rumus beriku:

f(1) == 1 

f(a) = 

Basis:
misalkan a == 1 maka fungsi akan mengembalikan nilai a (ini adalah stoping condition) setelah bertemu basis
fungsi akan bekerja secara LIFO (last in first out) seperti loop namun dibalik karena semua proses rekursi 
sebelumnya tersimpan didalam memori stack komputer yang umumnya bersifat LIFO, ini yang membuat rekursif 
memiliki kelemahan yaitu borosnya penggunaan memori yang banyak karena harus menyimpan subprogram pada satu
stack memory untuk setiap iterasi yang dilakukan sampai bertemu basisnya.

rekurens ganjil:

misalkan a > 1 dan a adalah ganjil dibuktikan dengan a modulo 2 == 1 maka akan mengembalikan rekurens nama
fungsinya sendiri namun parameter pr(a-1)==(genap) agar rekursi tidak infinite dan dikali dengan value
parameternya == (ganjil), karena itu saya menemukan fungsinya: 
jika a ganjil maka akan mengembalikan:
a x f(a-1)
a = angka ganjil tersebut
f(a-1) = angka genap dibawah a juga bertindak sebagai rekurens

rekurens genap:
misalkan a > 1 dan a adalah genap dibuktikan dengan a modulo 2 == 0 maka akan mengembalikan rekurens yaitu
value parameternya==(genap) dibagi 2 lalu dikali dengan pr(a-1)==(ganjil) agar rekursi tidak infinite loop,
karena itu saya menemukan fungsinya:
jika a genap maka akan mengembalikan:
(a/2) x f(a-1)
(a/2) = angka genap yang dibagi 2
f(a-1) = angka ganjil dibawah a juga bertindak sebagai rekurens
'''

def pr(a):
    if a == 1:
        return a
    elif a > 1 and (a%2==1):
        return a*pr(a-1)
    elif a > 1 and (a%2==0):
        return pr(a-1)*a/2

print(int(pr(7)))

#output = 630






