def wolo(s, i):
    if (len(s) == i):
        return ""
    else:
        return s[len(s)-i-1] +  wolo(s,i+1)

print(wolo("happy", 0))

##################

def home(x):
    if x<0:
        return 0
    else:
        return x + home(x-2)

print(home(5))

################

def tail(a,b,t):
    if b == 0:
        return t
    else:
        return tail(a,b-1,t*a)

print(tail(3,4,2))

#################

def box(a,b):
    if a>b:
        return 1+box(a-1,b)
    elif b>a:
        return 1+box(a,b-1)
    else:
        return a+b 

print(box(12,17))

#################

def jdd(x):
    if x <= 0:
        return 0
    else:
        return jdd(x//100) + x

print(jdd(19823))

################

def draw(x):
    if x > 0:
        draw(x-1)
        for i in range(x):
            print("*", end = "")
        print("")

print(draw(4))

#################

def job(a,b):
    if b==0:
        return 1
    elif b % 2 == 1:
        return a*job(a,b-1)
    else:
        temp = job(a,b/2)
        return temp*temp
        
print(job(2,5))
