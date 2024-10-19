import os
akuns = []

while True:
    print("Selamat datang di List Menu Nasi Goreng")
    print("1. Registrasi")
    print("2. Login")
    print("3. Exit")
    opsi = input("Pilih opsi: ")
    print(" ")

    if opsi == "1":
        print("Halo Pengguna baru! Ayo buat akun dulu")
        Username = input("Username: ")
        akuna = False
        for akun in akuns:
            if akun[0] == Username:  
                akuna = True
                break
        if akuna:
            print("nama kamu sudah di pakai. silahkan coba registrasi lagi")
        else:
            Password = input("Password: ")
            akuns.append([Username, Password, []])  
            print(f"Akun Anda berhasil terdaftar dengan ID: {Username}")


    elif opsi == "2":
        print("Hello, Kamu Login Dulu")
        Username = input("Username: ")
        Password = input("Password: ")
        for akun in akuns:
            if akun[0] == Username and akun[1] == Password:  
                while True:
                    print(f"\nSelamat datang {Username}!")
                    print("Silahkan Pilih opsi ini")
                    print("1. Pilih Menu")
                    print("2. Ubah Menu")
                    print("3. Tambah Menu")
                    print("4. Kembali")
                    
                    pilih = input("Pilih Nomor Menu: ")
                    print(" ")

                    if pilih == "1":
                        Daftar_Menu = {
                        "Menu 1" : "Nasi Goreng Biasa",
                        "Menu 2" : "Nasi Goreng Spesial",
                        "Menu 3" : "Nasi Goreng Pedas",
                        "Menu 4" : "Nasi Goreng Pattaya Seafood",
                        "Menu 5" : "Nasi Goreng Tom Yum",
                        "Menu 6" : "Nasi Goreng Extra Pedas",
                        "Menu 7" : "Nasi Goreng Sosis Bakso",
                        "Menu 8" : "Nasi Goreng Rendang"
                        }
                        print(Daftar_Menu["Menu 1"])
                        print(Daftar_Menu["Menu 2"])
                        print(Daftar_Menu["Menu 3"])
                        print(Daftar_Menu["Menu 4"])
                        print(Daftar_Menu["Menu 5"])
                        print(Daftar_Menu["Menu 6"])
                        print(Daftar_Menu["Menu 7"])
                        print(Daftar_Menu["Menu 8"])
                        print(Daftar_Menu)
                        
                    if pilih == "3":
                        opsi = input("opsi: ")
                        nomor = input("nomor: ")
                        akun[2].append([opsi, nomor]) 
                    else: 
                        print("list menu kamu sudah diubah!\n")
                        
                    if pilih == "4":
                       print("List Menu sudah kembali.\n")
                       break
         
                
    elif opsi == "3":
        print("kamu ingin keluar dari list menu ini? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("ketik pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah memilih menu ini, semoga bisa menikmatimu!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")     