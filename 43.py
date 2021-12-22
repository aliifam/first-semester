b = input()
s = input()

kertas = "[]"
batu = "()"
gunting = "8<"

if (b == kertas and s == kertas) or (b == batu and s == batu) or (b == gunting and s == gunting):
    print("Seri")
elif (b == kertas and s == batu) or (b == batu and s == gunting) or (b == gunting and s == kertas):
    print("Blangkon")
elif (s == kertas and b == batu) or (s == batu and b == gunting) or (s == gunting and b == kertas):
    print("Semar")
