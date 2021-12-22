def catatan():
    print("ketik 1 untuk Tambah catatan\nketik 2 untuk list catatan\nketik 3 untuk Keluar dari program")
    perintah = int(input())
    isi = []
    while perintah == 1:
        print("masukkan catatan yang ingin dimasukkan\nketik 2 untuk list catatan\nketik 3 untuk Keluar dari program")
        masukan = input()
        if masukan == "3":
            print("anda keluar dari program catatan dihapus semua")
            break
        elif masukan == "2":
            nomor = 0
            if len(isi) < 1:
                print("catatan masih kosong")
            else:
                print("berikut daftar catatan :")
                for i in isi:
                    nomor+=1
                    print(f"{nomor}. {i}")
        elif (masukan != "2") or (masukan != "3"): 
            isi.append(masukan)
catatan()

