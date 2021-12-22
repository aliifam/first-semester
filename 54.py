angka = input().split()

d1 = int(angka[0])
d2 = int(angka[1])
d3 = int(angka[2])

t1 = d1 + d2
t2 = d1 + d3
t3 = d2 + d3

lstangka = [t1, t2, t3]

print(max(lstangka))
