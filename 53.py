n = int(input())

templist = []

for jum in range(n):
    kata = input().split()
    
    for i in range(1, len(kata)):
        
        kata[i] = int(kata[i])
        
    if kata[0] == "insert":
        templist.insert(kata[1], kata[2])
    elif kata[0] == "append":
        templist.append(kata[1])
    elif kata[0] == "remove":
        templist.remove(kata[1])
    elif kata[0] == "pop":
        templist.pop()
    elif kata[0] == "sort":
        templist.sort()
    elif kata[0] == "reverse":
        templist.reverse()
    elif kata[0] == "print":
        print(templist)
