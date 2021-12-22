#modular rekursi fibonacci ke-n

def fib_ke_n(indeks):
    if indeks <= 2:
        return 1
    else:
        hasil = fib_ke_n(indeks-1) + fib_ke_n(indeks-2)
    return hasil

print(fib_ke_n(1))


