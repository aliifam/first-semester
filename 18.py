#aplikasi kalkulator
#(+-*/)
operasi = ""

while operasi != "exit":
    operasi = input("operasi = ")
    
    if operasi == "exit":
        break #force keluar dari while
    
    if operasi !="+" and operasi !="-" and operasi !="*" and operasi !="/":
        print("gunakan operator + - * /")
        continue #continue untuk mengulangi while dari awal
    
    a = int(input("Masukkan angka pertama = " ))
    b = int(input("Masukkan angka kedua = " ))
    
    if operasi == "+":
        result = a + b
    elif operasi == "-":
        result = a - b
    elif operasi == "*":
        result = a * b
    elif operasi == "/":
        result = a / b
    
    print("hasil = ", result)

print("anda keluar dari aplikasi")
