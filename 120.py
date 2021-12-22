#uas ppk no. 4

n = int(input())

x = list(map(int, input().split(" ")))
y = list(map(int, input().split(" ")))

x.sort()
y.sort()

temp = []
i = 0

while n > 0:
    jawaban = x[i] * y[i]
    temp.append(jawaban)
    i+=1
    n-=1

print(sum(temp))
