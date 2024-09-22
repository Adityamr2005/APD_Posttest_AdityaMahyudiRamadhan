Nama =input("masukin nama :")
Hari =input("masukin hari(Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, Minggu):")
Uang =input("masukin nominal uang saldo (Rp):")
Harga =input("masukin harga tiket di hari Senin-Minggu:")
Harga =input("masukin harga tiket di hari Jumat-Minggu:")
if Hari == ("Senin-Kamis") :
    Harga_Tiket = ("Rp 40000")
    if Uang < Harga_Tiket :
        print("uang saldo kamu tidak cukup beli tiket")
    else :
        print("terima kasih sudah membeli tiket di hari (Hari)")
elif Hari == ("Jumat") :
    Harga_Tiket = ("Rp 45000")
    if Uang < Harga_Tiket :
        print("uang saldo kamu tidak cukup beli tiket")
    else :
        print("terima kasih sudah membeli tiket di hari (Hari)")
elif Hari == ("Sabtu") :
    Harga_Tiket = ("Rp 55000")
    if Uang < Harga_Tiket :
        print("uang saldo kamu tidak cukup beli tiket")
    else :
        print("terima kasih sudah membeli tiket di hari (Hari)")
elif Hari == ("Minggu") :
    Harga_Tiket = ("Rp 60000")
    if Uang < Harga_Tiket :
        print("uang saldo kamu tidak cukup beli tiket")
    else :
        print("terima kasih sudah membeli tiket di hari (Hari)")
else :
    print("terima kasih sudah membeli tiket di hari lain")
        
        
        
    




    


    