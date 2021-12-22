#modular tierbesar dari tiga

def terbesar(a, b, c):
    max_ang = 0
    l_terbesar = [a,b,c]
    for i in l_terbesar:
        if i >= max_ang:
            max_ang = i
    return i
    
print(terbesar(3,2,3))
