#suit 5 kali

s_1 = input().split()
s_2 = input().split()
s_3 = input().split()
s_4 = input().split()
s_5 = input().split()

b = [s_1[0], s_2[0], s_3[0], s_4[0], s_5[0]]
s = [s_1[1], s_2[1], s_3[1], s_4[1], s_5[1]]

skor_b = 0
skor_s = 0

kertas = "[]"
batu = "()"
gunting = "8<"

for i in range(len(b)):
    if b[i] == s[i]:
        skor_s += 0
        skor_b += 0 
    elif (b[i] == gunting and s[i] == kertas) or (b[i] == batu and s[i] == gunting) or (b[i] == kertas and s[i] == batu):
        skor_b += 1
    elif (s[i] == gunting and b[i] == kertas) or (s[i] == batu and b[i] == gunting) or (s[i] == kertas and b[i] == batu):
        skor_s += 1

if skor_s == skor_b:
    print("Seri")
elif skor_s > skor_b:
    print("Semar")
elif skor_s < skor_b:
    print("Blangkon")

