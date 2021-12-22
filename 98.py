#sorting ppk

#bubble sort
none = int(input())
data = input().split()
data = list(map(int, data))
nuker = 0

for i in range(len(data)):
    for j in range(len(data)-1):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
            nuker += 1

output = ''
for k in data:
    output = output + str(k) + ' '
print(output)
print(nuker)

'''
#selection sort 
n = int(input())
data_2 = input().split()
data_2 = list(map(int, data_2))
nuker = 0

for a in range(len(data_2)-1):
    min_index = a
    for b in range(a+1, len(data_2)):
        if data_2[b] < data_2[min_index]:
            min_index = b
    if min_index != a:
         data_2[a], data_2[min_index] = data_2[min_index], data_2[a]
         nuker+=1

output = ""
for c in data_2:
    output = output + str(c) + " "

print(output)
print(nuker)
'''


