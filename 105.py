# -*- coding: utf-8 -*-
import os
boolean = True
jawabanBenarDibutuhkan = 0

def faktorial(n):
    if n == 1 or n == 0:
        return 1 
    else:
        return n * faktorial(n-1) 
def peluang(n, db):
    kombinasi = faktorial(n)/((faktorial(db)*faktorial(n-db)))
    kombinasi_new = "{:.0f}".format(kombinasi)
    kombinasiInt = float(kombinasi_new)
    peluangBenar = 1/5**db
    peluangBenar_new = "{:.80f}".format(peluangBenar)
    peluangBenarInt = float(peluangBenar_new)
    peluangSalah = (4/5)**(n-db)
    peluangSalah_new = "{:.10f}".format(peluangSalah)
    peluangSalahInt = float(peluangSalah_new)

    return kombinasiInt * peluangBenarInt * peluangSalahInt
while boolean == True:
    data = 0
    print("Program penghitung kemungkinan hoki :\n 1. Peluang UTUL UGM\n 2. Exit")
    pilihanProgram = int(input("Masukan pilihan: "))
    if pilihanProgram == 1:
        passingGradeProgramStudi = float(input("Masukan passing grade program studi (0 < pg < 1) : "))
        jawabanYakinBenar = int(input("Masukan jawaban yakin benar : "))
        jawabanNgawur = int(input("Masukan jawaban ngawur : "))
        jawabanKosong = 180 - jawabanYakinBenar - jawabanNgawur
        poinMaksimal = 180*4
        passingGrade = passingGradeProgramStudi * poinMaksimal
        poinAwal = (jawabanYakinBenar*4)
        poinDibutuhkan = int(passingGrade - poinAwal)
        poinTerdefinisiSalah = (jawabanYakinBenar*4) + (jawabanNgawur*-1)
        if poinTerdefinisiSalah >= passingGrade:
            print("100%")
            break
        for i in range(1,jawabanNgawur+1):
            temp = ((i)*4) + (jawabanNgawur-i)*-1
            if temp >= poinDibutuhkan:
                jawabanBenarDibutuhkan = i
                break
            if (i) == jawabanNgawur:
                print("tidak ditemukan peluang anda, silahkan coba lagi tahun depan\n")
                quit()
        for p in range(jawabanBenarDibutuhkan, jawabanNgawur+1):
            data += peluang(jawabanNgawur, p) * 100

        print(data,"%\n\n")
    elif pilihanProgram == 2:
        quit()
    else:
        os.system("clear")
        print("Masukan angka di dalam list!")
        continue
