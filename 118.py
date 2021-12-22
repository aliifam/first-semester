#ppk no.2

n = int(input())

nl = list(map(int, input().split(" ")))

temp = []

for i in nl:
    if len(temp) == 0:
        temp.append(i)
    elif len(temp) % 2 == 0:
        temp.insert(int(len(temp)/2), i)
    elif len(temp) % 2 != 0:
        temp.insert(int(len(temp)/2), i)

jawaban = " ".join(map(str, temp))

print(jawaban)
