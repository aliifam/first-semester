#ppkuas no. 5

n = input().split("00")

temp = []

for i in n:
    awal = 0
    for j in i:
        if j == "1":
           awal = awal + 1
           temp.append(awal)

print(sum(temp))
