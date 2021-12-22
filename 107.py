#program operasi dalam kata 
import re

kata_ekstrak = []
list_jumlah = []
list_terbanyak = []
list_tersedikit = []

def ekstrak_kata(kata):
    kata = kata.lower()
    kata = list(filter(None, re.split("[,. \-!?:]+", kata))) #<<=MENGGUNAKAN REGEX UNTUK SPLITTING CHAR
    for i in kata:
        if i not in kata_ekstrak:
            kata_ekstrak.append(i)

def jumlah_kata(kata):
    kata = kata.lower()
    kata = list(filter(None, re.split("[,. \-!?:]+", kata))) #<<=MENGGUNAKAN REGEX UNTUK SPLITTING CHAR
    for i in kata_ekstrak:
        temp = 0
        for j in kata:
            if j == i:
                temp = temp + 1
        list_jumlah.append(temp)

def properti_kata(kata):
    for i in range(len(kata_ekstrak)):
        katanya = kata_ekstrak[i]
        munculnya = list_jumlah[i]
        print(f'- "{katanya}" muncul sebanyak = {munculnya} kali')

def terbanyak(kata):
    i = max(list_jumlah)
    for j in range(len(list_jumlah)):
        if list_jumlah[j] == i:
            list_terbanyak.append(kata_ekstrak[j])
    kata_terbanyak = " \n- ".join(list_terbanyak)
    print(f'kata terbanyak yang muncul dalam kalimat adalah = \n- {kata_terbanyak}')

def tersedikit(kata):
    i = min(list_jumlah)
    for j in range(len(list_jumlah)):
        if list_jumlah[j] == i:
            list_tersedikit.append(kata_ekstrak[j])
    kata_tersedikit = " \n- ".join(list_tersedikit)
    print(f'kata tersedikit yang muncul dalam kalimat adalah = \n- {kata_tersedikit}')

def operasi(loh):
    ekstrak_kata(loh)
    jumlah_kata(loh)
    properti_kata(loh)
    terbanyak(loh)
    tersedikit(loh)
    
    

kalimat = input("masukkan kalimat anda = ")
operasi(kalimat)


