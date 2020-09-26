import random
import datetime
from customer import Customer

atm = Customer (id)

while True:
    id = int(input("Masukkan pin anda: "))
    trial = 0
    while (id != int(atm.checkPin()) and trial < 3):
        id = int(input("Pin anda salah. Silahkan Masukkan Lagi: "))

        trial += 1
        if trial == 3:
            print("Error. Silahkan ambil kartu dan coba lagi..")
            exit()

            while True:
                print("Selamat datang di atm ku...")
                print("\n1 - Cek Saldo \t 2 - Debet \t 3 - Simpan \t 4 - Ganti Pin \t 5 - Keluar")

            selectmenu = int (input("\nSilakan pilih menu: "))

            if selectmenu == 1:
                print("\nSaldo anda sekarang: Rp. " + str(atm.checkBalance()) + "\n")

            elif selectmenu == 2:
                nominal = float(input("Masukkannominal saldo: "))
                verify_withdraw = input("konfirmasi: Anda akan melakukkan debet dengan nominal berikut ? y/n " + str(nominal) + " ")
            if verify_withdraw == "y":
                print("saldo awal anda adalah: Rp. " + str(atm.checkBalance()) + "")
            else:
                break
            if nominal < atm.checkBalance():
                atm.withdrawBalance(nominal)
                print("Transaksi debet berhasil!")
                print("Saldo sisa sekarang: Rp. " + str(atm.check.Balance()) + "")
            else:
                print("Maaf. saldo anda tidak cukup untuk melakukan debet!")
                print("Silahkan lakukan penambahan nominal saldo")

            elif selectmenu == 3:
                nominal = float(input("Masukkan nominal saldo: "))
                verify_deposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n " + str(nominal) + " ")

                if verify_deposit == "y":
                    atm.depositBalance(nominal)
                    print("Saldo anda sekarang adalah: Rp. " + str(atm,checkBalance()) + "\n" )
            else:
                break


            elif selectmenu == 4:
                verify_pin = int(input("masukkan pin anda")

                while verify_pin != int(atm.checkPin()):
                    print("pin anda salah, silahkan masukkan pin: ")

                update_pin = int(input("silahkan masukkan pin yang baru: "))
                print("pin anda berhasil diganti! ")

                verify_newpin = int(input("coba masukkan pin baru: "))


                if verify_newpin == update_pin:
                    print("pin baru anda sukses!")

                else:
                    print("maaf, pin anda salah")

            elif selectmenu == 5:
                print("Resi tercetak otomatis saat anda keluar. \n Harap simpan tanda terima ini \n sebagai bukti transaksi anda.")
                print("No. Rekord: ", random.randint(100000,1000000))
                print("Tanggal: ", datetime.datetime.now())
                print("Saldo akhir: ", atm.checkBalance())
                print("tenkkyu")
                exit()