#Modular prog

def is_primer(x):
    primer = False
    if x>1:
        for i in range(2, x):
            if x % i == 0:
                primer = True
    return primer

print(is_primer(1))




def cetak(jawaban):
    print(jawaban)

def maksimal(a,b,c):
    jek = 0
    if a >= b and a >= c:
        jek = a
    elif b >= a and b >= c:
        jek = b
    elif c >= a and c >= b:
        jek = c
    return jek
    
cetak(maksimal(3,4,6))





