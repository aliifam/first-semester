#adp uas no. 3

b1 = input().split(" ")

n = int(b1[0])
k = int(b1[1])

b2 = input().split(" ")
b2 = list(map(int, b2)) #list dari Pi setiap index list itu Pi jarak

b3 = input().split(" ")
b3 = list(map(int, b3)) #list dari Ai setiale index list itu Ai

jn = 0
'''
for i in range(0, k):
    if b3[i] > b2[i]:
        b3[i] = b3[i] - b2[i]
        jn+=1
    print(jn)'''

for i in b3:
    temp = []
    for j in b2:
        if i > sum(b2):
            jawaban = len(b2)
        else:
            if i > j:
                i = i - j
                temp.append(j)
                jawaban = len(temp)
    print(jawaban)

'''
input = 
5 5
1 2 1 2 1
2 3 5 6 10

output = 
1
2
3
4
5
'''
    




