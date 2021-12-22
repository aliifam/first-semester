n = input()

a = n.split(" ")
for i in range(len(a)):
    a[i] = a[i].capitalize()
    t = " ".join(a)
print(t)
