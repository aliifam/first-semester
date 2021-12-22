import math

alas = float(input())
tinggi = float(input())

simir = (alas/2)**2  + (tinggi**2)

simirfix = math.sqrt(simir)

k = alas + simirfix + simirfix

print("{:.2f}".format(k))
