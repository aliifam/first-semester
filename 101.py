#aneh
'''
def aneh(n):
    if n == 0:
        return 10
    elif (n>0) and (n%2==0):
        return 4*aneh(n/2)
    else:
        return aneh(n-1)+1

a = int(input())
print(aneh(a))'''

'''
#radar
data = input().split()
n = int(data[0])
x1 = int(data[1])
y1 = int(data[2])
x2 = int(data[3])
y2 = int(data[4])

pen = []

for i in range(n):
    for j in range(n):
        if j == y1 and i == x1:
            pen.append("o")
        elif j == y2 and i == x2:
            pen.append("x")
        else:
            pen.append(".")
    print("".join(pen))
    pen.clear()
'''

#radar 2 
n = int(input())
data = list(map(int, input().split()))
data2 = list(map(int, input().split()))
data3 = list(map(int, input().split()))

pen = []

for i in range(n):
    for j in range(n):
        if j == data[1] and i == data[0]:
            pen.append("o")
        elif j == data[3] and i == data[2]:
            pen.append("x")
        else:
            pen.append(".")
    print("".join(pen))
    pen=[]

print("")    

for i in range(n):
    for j in range(n):
        if j == data2[1] and i == data2[0]:
            pen.append("o")
        elif j == data2[3] and i == data2[2]:
            pen.append("x")
        else:
            pen.append(".")
    print("".join(pen))
    pen=[]

print("")    

for i in range(n):
    for j in range(n):
        if j == data3[1] and i == data3[0]:
            pen.append("o")
        elif j == data3[3] and i == data3[2]:
            pen.append("x")
        else:
            pen.append(".")
    print("".join(pen))
    pen=[]


