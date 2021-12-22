#nilai kelulusan

a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = int(input())

list_nilai = [a,b,c,d,e]
n = 0
for item in range(0, len(list_nilai)):
    if list_nilai[item] >= f:
        n = n + 1 
print(n)

