def print1(x):
    for i in range(x):
        print('X', end='')
    print('.', end='')
    
def print2(x):
    for i in range(1, x+1):
        print1(i)

print2(3)

###############################

a = 2
def t1(x):
    a = x

def t2(x):
    global a
    a = int(x)
    
t1(3)
t2(4)
print(a)
