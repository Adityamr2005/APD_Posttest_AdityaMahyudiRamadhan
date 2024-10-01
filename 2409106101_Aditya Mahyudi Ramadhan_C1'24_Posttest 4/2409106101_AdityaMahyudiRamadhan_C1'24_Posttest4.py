print("selamat datang")

salah = 0
while salah < 3:
    
    username = input("silahkan ketik username kamu:")
    password = int(input("silahkan ketik password kamu:"))
    if username == "adit-kun" and password == 101:
        lanjut = input("kamu akan lanjutkan atau hentikan login?")
        if lanjut == "hentikan":
            print("program kamu sudah berhenti")
        else:
            print("selamat kamu bisa login!")
        Hari =str(input("masukin hari(Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu):"))
        Uang = int(input("masukin nominal uang saldo (Rp):"))
        if Hari == "senin" or Hari == "selasa" or Hari == "rabu" or Hari == "kamis":
           if Uang < 40000 :
               print("uang saldo kamu tidak cukup beli tiket")
               break
           else :
               print(f"terima kasih sudah membeli tiket di hari {Hari}")
               break
        elif Hari == ("Jumat") :
            if Uang < 45000 :
                print("uang saldo kamu tidak cukup beli tiket")
                break
            else :
                print(f"terima kasih sudah membeli tiket di hari jumat")
                break
        elif Hari == ("Sabtu") :
            if Uang < 55000 :
                print("uang saldo kamu tidak cukup beli tiket")
                break
            else :
                print(f"terima kasih sudah membeli tiket di hari sabtu")
                break
        elif Hari == ("Minggu") :
            if Uang < 60000 :
                print("uang saldo kamu tidak cukup beli tiket")
                break
            else :
                print(f"terima kasih sudah membeli tiket di hari minggu")
                break
        else :
            print(f"nama hari yang kamu pilih tidak valid")
            break
    else:
        print("usr dan pw yang kamu masukin salah")
        lanjut = input("kamu lanjutkan atau hentikan?:")
        if lanjut == "hentikan":
            print("program kamu sudah berhentikan")
        else:
            salah = salah + 1
            print(f"kamu sudah mencoba sebanyak {salah} kali")
    

        