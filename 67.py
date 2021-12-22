#max algo

n = int(input())

anglst = []

for i in range(n):
    in_ang = int(input())
    anglst.append(in_ang)
    
max_ang = 0
    
for i in anglst:
    if (i>max_ang):
        max_ang = i

max_ang_2 = 0

for i in anglst:
    if (i<max_ang) and (i>max_ang_2):
        max_ang_2 = i

max_ang_3 = 0

for i in anglst:
    if (i<max_ang) and (i>max_ang_2) and (i<max_ang_3):
        max_ang_3 = i


print(max_ang)
print(max_ang_2)
print(max_ang_3)

