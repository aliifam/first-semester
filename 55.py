b1 = input().split()
b2 = input().split()
b3 = input().split()
b4 = input().split()

a = int(b1[0])
b = int(b1[1])
c = int(b2[0])
d = int(b2[1])

e = int(b3[0])
f = int(b3[1])
g = int(b4[0])
h = int(b4[1])

hasil_a = (a*e) + (b*g)
hasil_b = (a*f) + (b*h)
hasil_c = (c*e) + (d*g)
hasil_d = (c*f) + (d*h)

print(hasil_a, hasil_b)
print(hasil_c, hasil_d)



