#calculator ITS

n = input().split(" ")

list_angka = []

list_oper = []

for i in range(len(n)):
    if i % 2 == 0:
        list_angka.append(n[i])
    else:
        list_oper.append(n[i])

list_angka = list(map(int, list_angka))

plus = "+"
minus = "-"
divide = "/"
kali = "*"
pang = "^"

gerak = len(n)

l_jaw = []

for j in range(0, len(list_oper), 2):
    if list_oper[j] == plus:
        jawaban = list_angka[j] + list_angka[j+1]
        l_jaw.append(jawaban)
    elif list_oper[j] == minus:
        jawaban = list_angka[j] - list_angka[j-1]
        l_jaw.append(jawaban)
    else:
        jawaban = list_angka[j]
        l_jaw.append(jawaban)
    jawaban = 0

print(list_angka)
print(list_oper)
print(l_jaw)

#1 + 2 + 3 - 4 int(float(coffee_bags))

