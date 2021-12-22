#rekursi fab

def f(a,b):
    if b == 0:
        return 1
    else:
        return a * f(a, b-1)

print(f(2,3))

def tabung(m, i, n): #n bulan i bunga m tabungan
    if n < 1:
        return m + m*i*n
    else:
        return tabung(m, i, n-1) * (1+i)

print(tabung(1,1,0))



# -1 + 2 -3 + 4
def aneh(d):
    if d == 1:
        return -d
    if (d>1) and (d%2 == 1):
        return aneh(d-1)-d
    elif (d>1) and (d%2 == 0):
        return aneh(d-1)+d

print(aneh(2))







