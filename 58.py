nilai = input().split()
kkm = float(input())

n1 = float(nilai[0])
n2 = float(nilai[1])
n3 = float(nilai[2])
n4 = float(nilai[3])
n5 = float(nilai[4])

listnil = [n1, n2, n3, n4, n5]

tot = 0

for i in listnil:
    if i >= kkm:
        tot += 1 

print(tot)
    
