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
                    print("3. Isi Data Pemesan")
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
                    elif pilih == "2":
                        if not akun[2]:
                           print("Silahkan lihat menu ini.")
                        else:
                            def Daftar_Menu():
                                print ("\n")
                                print ("----------- MENU---------- ")
                                print ("[1] Nasi Goreng Biasa")
                                print ("[2] Nasi Goreng Spesial")
                                print ("[3] Nasi Goreng Pedas")
                                print ("[4] Nasi Goreng Pattaya Seafood")
                                print ("[5] Nasi Goreng Tom Yum")
                                print ("[6] Nasi Goreng Extra Pedas")
                                print ("[7] Nasi Goreng Sosis Bakso")
                                print ("[8] Nasi Goreng Rendang")
                            menu = input("PILIH MENU> ")
                            print ("\n")
                            if menu == "1":
                               Nasi_Goreng_Biasa()
                            elif menu == "2":
                               Nasi_Goreng_Spesia()
                            elif menu == "3":
                               Nasi_Goreng_Pedas()
                            elif menu == "4":
                               Nasi_Goreng_Pattaya_Seafood()
                            elif menu == "5":
                               Nasi_Goreng_Tom_Yum()
                            elif menu == "6":
                               Nasi_Goreng_Extra_Pedas()
                            elif menu == "7":
                               Nasi_Goreng_Sosis_Bakso()
                            elif menu == "8":
                               Nasi_Goreng_Rendang()
                             
                            else:
                                print ("Silahkan pilih salah satu menu ini")
    
                            while (True):
                                show_menu()
                    if pilih == "3":
                        def info():
                            
                          username = "Adityamr"
                          pilih_menu = "Nasi Goreng Spesial"
                          print("Nama Pemesan:", username)
                          print("Pilih Menu:", pilih_menu)
                        
                        info()               
                        
                    if pilih == "4":
                       def ucapan():
                           print ("Terima Kasih sudah memilih menu ini!")
                           
                           ucapan()
         
                
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