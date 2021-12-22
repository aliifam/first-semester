#ppk rekursif

def f(a):
    if a < 1:
        return a
    elif a % 2 == 0:
        return f(a-1) + a
    else:
        return f(a-1) - a

print(f(2))

def z(x):
    if x <= 1:
        return x 
    else:
        return x + z(1/x-1)

print(z(2))

#pascal triangle
def pt(x,y):
    if x==0 or y==0:
        return 1
    else:
        return pt(x-1, y-1) + pt(x-1, y)
        
print(pt(3,2))

#rekursif pangkat
def pangkat(a, n):
    if n < 1:
        return 1
    else:
        return a*pangkat(a, n -1)

print(pangkat(2,2))

#bakteri memebelah 2 setiap saru jam awal 5 bakteri
def jb(awal, jam):
    if jam <= 1:
        return awal
    else:
        return jb(awal, jam-1)*2

print(jb(5, 4))




