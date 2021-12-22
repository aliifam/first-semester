#insertion
'''
n = int(input())
data = list(map(int, input().split()))
nuker = 0

for i in range(1, len(data)):
    nilai_t = data[i]
    posi_t = i
    
    while posi_t > 0 and data[posi_t - 1] > nilai_t:
        data[posi_t] = data[posi_t - 1]
        posi_t = posi_t - 1 
    if posi_t != i:     
        data[posi_t] = nilai_t
        nuker += 1
    
output = ''
for j in data:
    output = output + str(j) + ' '
    
print(output)
print(nuker)
'''

def ascend_sort(the_list):
    for i in range(len(the_list)):
        for j in range (len(the_list) - 1):
            if the_list[j] >= the_list[j+1]:
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
    return the_list
    
def descend_sort(the_list):
    for i in range(len(the_list)):
        for j in range (len(the_list) - 1):
            if the_list[j] <= the_list[j+1]:
                the_list[j], the_list[j+1] = the_list[j+1], the_list[j]
    return the_list

n = int(input())
the_list = list(map(int, input().split()))
bat = input().split()
bawah = int(bat[0])
atas = int(bat[1])
mode = bat[2]

output = ""

if mode == "A":
    sem = []
    for k in range(atas):
        sem.append(the_list[k])
    ascend_sort(sem)
    for z in sem:
        output = output + str(z) + " "
    print(output)
elif mode == "D":
    sem = []
    for k in range(atas):
        sem.append(the_list[k])
    descend_sort(sem)
    for z in sem:
        output = output + str(z) + " "
    print(output)


