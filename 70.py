#nomor 3 dan 4
N = int(input())
nilai = input().split(" ")

listnil = []

for i in nilai:
    i = float(i)
    listnil.append(i)

max_ang = 0

for j in listnil:
    if j > max_ang:
        max_ang = j
    
jum_sis = 0 

for k in listnil:
    if k == max_ang:
        jum_sis+=1

print(jum_sis)

