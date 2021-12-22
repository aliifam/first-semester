#pr adp 4, Count occurrences of a number in a sorted array approach binary search

def binary_so(data, n):
    
    data.sort() #sorting data list agar binary search bisa berjalan
    
    awal = 0 #index awal untuk binary search
    akhir = len(data) - 1 #index akhir untuk binary search
    
    while awal <= akhir:
        
        tengah = (awal + akhir) // 2
        
        tebakan = data[tengah]
        
        if n == tebakan:
            kanan = tengah + 1 #untuk pergerakan index ke kanan penghitungan jumlah kemunculan angka 
            kiri = tengah - 1 #untuk pergerakan index ke kiri penghitungan jumlah kemunculan angka 
            ke_kanan = 0 #untuk awal kemunculan ke kanan penghitungan jumlah kemunculan angka 
            ke_kiri = 0 #untuk awal kemunculan ke kiri penghitungan jumlah kemunculan angka 
            akhiran = -1
            if tebakan < data[-1]: #kondisi ketika angka yang dicari tidak lebih besar dari max angka dalam list
                while (tebakan == data[kanan] or tebakan == data[kiri]):
                    if tebakan == data[kanan]:
                        ke_kanan += 1
                        kanan +=1
                    elif tebakan == data[kiri]:
                        ke_kiri += 1
                        kiri -=1
            elif data[0] == data[-1] and data[-1] == tebakan: #kondisi ketika angka yang didalam list sama semua
                ke_kiri = len(data) - 1
            else: #kondisi ketika angka yang dicari paling besar di dalam list
                while tebakan == data[akhiran - 1]:
                    if tebakan == data[akhiran - 1]:
                        ke_kiri += 1
                        akhiran -=1
            total = ke_kanan + ke_kiri + 1
            n = str(n)
            total = str(total)
            jawaban = "angka: "+ n + "\nmuncul: "+ total + " kali dalam list"
            return jawaban
            
        elif n < tebakan:
            akhir = tengah - 1
            
        elif n > tebakan:
            awal = tengah + 1
            
    return "angka yang anda cari tidak adal dalam list"
    
list_n = [1,2,3,4,5,6,6,6,7]
print(binary_so(list_n, 6))

#output:
#angka: 6
#muncul: 3 kali dalam list
