ukuran = input().split()

B = int(ukuran[0])
P = int(ukuran[1])
L = int(ukuran[2])

if (B + P + L <= 140):
    print("S")
elif (B + P + L <= 194):
   print("M")
elif (B + P + L <= 278):
   print("L")
else:
   print("X")