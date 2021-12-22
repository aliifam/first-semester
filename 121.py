#ppk no 6 

sj = int(input())
sm = int(input())
bj = int(input())
bm = int(input())

st = (sj * 60) + sm
bt = (bj * 60) + bm 

if st < bt:
    print("SEMAR")
else:
    print("BAGONG")
