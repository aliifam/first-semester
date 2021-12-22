import math

a = float(input())
b = float(input())
c = float(input())

d = (b**2) - (4*a*c)

#x1 dan x2
x1 = (-b+math.sqrt(d))/(2*a)
x2 = (-b-math.sqrt(d))/(2*a)

print(int(x1), int(x2))


