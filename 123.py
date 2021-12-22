#ppkuasno8

import sys

n = int(input())

if  0 <= n <= 10000000000:
    has = 2 ** n
else:
    sys.exit()
    

has = str(has)

jawaban = has[-1]

jawaban = int(jawaban)

print(jawaban)

