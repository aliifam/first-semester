p = int(input())
t = input().split()

f = []

for a in t:
    a = int(a)
    f.append(a)

sisap = p

lsisap = []

for j in range(len(f)):
    awal = 0
    if sisap >= f[j]:
        sisap = sisap - f[j]
        lsisap.append(f[j])
    else:
        sisap = 0

print(len(lsisap))

