n = int(input()) #masukkan 3

awal , akhir = 0,1 

kond = 0

while kond < n: #ketika 0 < 3, 1<3
    jaw = awal + akhir #jaw = 0+1 jaw = 1+1
    awal = akhir       #awal = 1, awal = 1 
    akhir = jaw        #akhir = 1 akhir = 2
    kond += 1          # kond = 0 + 1   
    
print("bilangan fibonacci ke",n,"=",awal)


