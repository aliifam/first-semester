#modular void function menmbahkan jumlah element list

L = [1,2,3,4,5,6,7,8,9]

def tambahelemen(bilx):
    hasil = []
    for i in L:
        i = i + bilx
        hasil.append(i)
    return hasil

print(tambahelemen(1))
