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
                    print("2. Kembali")

                    pilih = input("Pilih Nomor Menu: ")
                    print(" ")

                    if pilih == "1":
                        status = ("Nasi Goreng Biasa", "Nasi Goreng Spesial", "Nasi Goreng Pedas", "Nasi Goreng Pattaya Seafood", "Nasi Goreng Tom Yum", "Nasi Goreng Extra Pedas", "Nasi Goreng Sosis Bakso", "Nasi Goreng Rendang")
                        nomor = print("")             
                        print("Menu kamu sudah dipilih!\n")
                        
                    elif status == "2":
                        print("menu kamu sudah ditutup.\n")
                        break

    elif opsi == "3":
        print("kamu ingin keluar dari menu ini? ")
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