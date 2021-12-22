name = input().split(" ")

name = list(name)

huruf = []

for i in name:
    awal = 0
    for j in i:
        if (j=="a") or (j=="e"):
            awal += 1
    huruf.append(awal)

patok = 0

for k in range(len(huruf)):
    if huruf[k] > patok:
        patok = huruf[k]
        namefix = name[k]

print(namefix)

