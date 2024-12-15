import os
import datetime
import random

def clear_screen():
    os.system('cls')

def generate_invoice():
    return f"INV/{datetime.datetime.now().strftime('%Y%m%d')}/{random.randint(1000,9999)}"

clear_screen()

print("|=======================================|")
print("| Halo! Selamat datang di layanan kami! |")
print("|=======================================|")
print()
nama_user = input("Pesanan atas nama? ")
nomor_antrian = random.randint(1, 100)
print()
print("========================================================")
print(f" Terima kasih, {nama_user}! Nomor antrian Anda adalah {nomor_antrian}.")
print("========================================================")

def makanan():
    global total_makan, pesan_makan, jumlah_porsi
    total_makan = 0
    pesan_makan = []

    while True:
        print("-------------------------------------------------")
        print("             : Pilih Menu Makanan :              ")
        print("-------------------------------------------------")
        print("1.  Nasi Goreng Kampung                Rp. 18.000")
        print("2.  Nasi Goreng Spesial                Rp. 20.000")
        print("3.  Indomie Polos                      Rp. 8.000 ")
        print("4.  Indomie Telur                      Rp. 12.000")
        print("5.  Indomie Telur Kornet               Rp. 15.000")
        print("6.  Nasi Ayam Geprek                   Rp. 15.000")
        print("7.  Nasi Ayam Kremes                   Rp. 18.000")
        print("8.  Nasi Telur Dadar                   Rp. 10.000")
        print("9.  Chicken Wings                      Rp. 25.000")
        print("10. French Fries                       Rp. 15.000")
        print("11. Mix Platter                        Rp. 20.000")
        print("12. Cireng Bumbu Rujak                 Rp. 12.000")
        print("13. Roti Bakar                         Rp. 15.000")
        print("14. Pisang Bakar                       Rp. 12.000")
        print("15. Risol Mayo                         Rp. 15.000")
        print("0.  Untuk selesai memesan makanan                ")
        print("-------------------------------------------------")
        
        try:
            menu_makanan = int(input("Silahkan pilih menu, masukan angka 0 untuk selesai: "))
            if menu_makanan == 0:
                break
            
            if menu_makanan not in range (1, 16):
                print("Pilihan tidak tersedia. Silakan pilih menu yang tersedia.")
                continue

            jumlah_porsi = int(input("Masukan jumlah porsi: "))
            if jumlah_porsi < 1:
                print("Jumlah pesanan harus lebih dari 0.")
                continue

            menu_dict = {
                1: ("Nasi Goreng Kampung", 18000),
                2: ("Nasi Goreng Spesial", 20000),
                3: ("Indomie Polos", 8000),
                4: ("Indomie Telur", 12000),
                5: ("Indomie Telur Kornet", 15000),
                6: ("Nasi Ayam Geprek", 15000),
                7: ("Nasi Ayam Kremes", 18000),
                8: ("Nasi Telur Dadar", 10000),
                9: ("Chicken Wings", 25000),
                10: ("French Fries", 15000),
                11: ("Mix Platter", 20000),
                12: ("Cireng Bumbu Rujak", 12000),
                13: ("Roti Bakar", 15000),
                14: ("Pisang Bakar", 12000),
                15: ("Risol Mayo", 15000),}

            nama_menu, harga_satuan = menu_dict[menu_makanan]

            total = jumlah_porsi * harga_satuan
            pesan_makan.append((nama_menu, jumlah_porsi, total))
            
            total_makan += total

        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")

def minuman():
    global total_minum, pesan_minum, jumlah_gelas
    total_minum = 0
    pesan_minum = []

    while True:
        print("-------------------------------------------------")
        print("             : Pilih Menu Minuman :              ")
        print("-------------------------------------------------")
        print("1.  Es Teh Maniez                      Rp. 5.000 ")
        print("2.  Lemon Tea                          Rp. 8.000 ")
        print("3.  Teh Tarik                          Rp. 10.000")
        print("4.  Bubble Milk Tea                    Rp. 15.000")
        print("5.  Americano                          Rp. 8.000 ")
        print("6.  Kopi Tubruk                        Rp. 8.000 ")
        print("7.  Latte                              Rp. 15000 ")
        print("8.  Cappucino                          Rp. 12.000")
        print("9.  Hot Chocolatte                     Rp. 10.000")
        print("10. Matcha                             Rp. 10.000")
        print("11. Fresh Juice                        Rp. 12.000")
        print("12. Jeruk Peras                        Rp. 10.000")
        print("13. Susu Jahe                          Rp. 10.000")
        print("14. Soda Gembira                       Rp. 12.000")
        print("15. Air Mineral                        Rp. 5.000 ")
        print("0.  Untuk selesai memesan minuman                ")
        print("-------------------------------------------------")
        
        try:
            menu_minuman = int(input("Silahkan pilih menu, masukan angka 0 untuk selesai: "))
            if menu_minuman == 0:
                break
            
            if menu_minuman not in range (1, 16):
                print("Maaf menu tidak tersedia. Silakan pilih menu yang tersedia.")
                continue

            jumlah_gelas = int(input("Masukan jumlah gelas: "))
            if jumlah_gelas < 1:
                print("Jumlah pesanan harus lebih dari 0.")
                continue

            menu_dict = {
                1: ("Es Teh Maniez", 5000),
                2: ("Lemon Tea", 8000),
                3: ("Teh Tarik", 10000),
                4: ("Bubble Milk Tea", 15000),
                5: ("Americano", 8000),
                6: ("Kopi Tubruk", 8000),
                7: ("Latte", 15000),
                8: ("Cappuccino", 12000),
                9: ("Hot Chocolate", 10000),
                10: ("Matcha", 10000),
                11: ("Fresh Juice", 12000),
                12: ("Jeruk Peras", 10000),
                13: ("Susu Jahe", 10000),
                14: ("Soda Gembira", 12000),
                15: ("Air Mineral", 5000),
            }
            
            nama_menu, harga_satuan = menu_dict[menu_minuman]

            total = jumlah_gelas * harga_satuan
            pesan_minum.append((nama_menu, jumlah_gelas, total))
            
            total_minum += total

        except ValueError:
            print("Input tidak valid. Silakan masukkan angka yang benar.")

def promo(total):
    promo_codes = {
        "DISKON10": 0.10,  
        "DISKON20": 0.20,  
        "BARU": 0.15,      
    }
    
    kode_promo = input("Masukkan kode promo (atau tekan Enter jika tidak ada): ")
    
    if kode_promo in promo_codes:
        diskon = promo_codes[kode_promo]
        total_diskon = total * diskon
        total -= total_diskon
        print(f"Diskon {diskon * 100}% diterapkan. Total setelah diskon: Rp. {total}")
    else:
        print("Kode promo tidak valid atau tidak ada diskon yang diterapkan.")
    
    return total

def simpan_ke_file(nama_file, nama_user, nomor_antrian, pesan_makan, pesan_minum, subtotal, diskon, ppn, total_akhir):
    with open(nama_file, 'a') as file:
        file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        invoice_number = generate_invoice()
        file.write("\n=======================================================\n")
        file.write(f"Invoice: {invoice_number}\n")
        file.write(f"Waktu Transaksi      : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("=======================================================\n")
        file.write("                    DETAIL PEMBELIAN                  \n")
        file.write("=======================================================\n")
        file.write(f"Nama Pelanggan: {nama_user}\n")  
        file.write(f"Nomor Antrian : {nomor_antrian}\n") 
        file.write("MAKANAN:\n")
        for item in pesan_makan:
            file.write(f"- {item[0]:<25} {item[1]:<10} = Rp. {item[2]:<20}\n")
        file.write("\nMINUMAN:\n")
        for item in pesan_minum:
            file.write(f"- {item[0]:<25} {item[1]:<10} = Rp. {item[2]:<20}\n")
        file.write("\n=======================================================\n")
        file.write(f"Subtotal              : Rp. {subtotal}\n")
        file.write(f"Diskon                : Rp. {diskon}\n")
        file.write(f"PPN 10%               : Rp. {ppn}\n")
        file.write(f"Total Akhir           : Rp. {total_akhir}\n")
        file.write("=======================================================\n")
        file.write("\n")
        file.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")


def main():
    global total_makan, total_minum, pesan_makan, pesan_minum
    total_makan = 0
    total_minum = 0
    pesan_makan = []
    pesan_minum = []

    while True:
        makanan()
        clear_screen()
        minuman()
        clear_screen()

        subtotal = total_makan + total_minum
        subtotal = promo(subtotal)
        diskon = total_makan + total_minum - subtotal if subtotal < (total_makan + total_minum) else 0
        ppn = round(subtotal * 0.1)
        total_akhir = round(subtotal + ppn)

        print("--------------------------------------------------------")
        print("                    Daftar  Pembelian                   ")
        print("--------------------------------------------------------")
        print(f"Nama Pelanggan: {nama_user}")  
        print(f"Nomor Antrian : {nomor_antrian}") 
        print(f"Tanggal       : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("--------------------------------------------------------")
        print("MAKANAN:")
        for item in pesan_makan:
            print(f"- {item[0]:<25} {item[1]:<10} = Rp. {item[2]:<20}\n")
        print("MINUMAN:")
        for item in pesan_minum:
            print(f"- {item[0]:<25} {item[1]:<10} = Rp. {item[2]:<20}\n")
        print("--------------------------------------------------------")
        print(f" Subtotal             : Rp. {subtotal}")
        print(f" Diskon               : Rp. {diskon}")
        print(f" PPN 10%              : Rp. {ppn}")
        print(f" Total Akhir          : Rp. {total_akhir}")
        print("--------------------------------------------------------")

        simpan_ke_file('daftar_pembelian.txt', nama_user, nomor_antrian, pesan_makan, pesan_minum, subtotal, diskon, ppn, total_akhir)

        
        while True:
            if total_akhir == 0:
                print("Anda tidak memesan apapun.")
                break
            else:
                try:
                    uang_bayar = int(input("Masukan uang anda: Rp. "))
                    if uang_bayar < total_akhir:
                        kekurangan = total_akhir - uang_bayar
                        print(f"Maaf, uang Anda kurang Rp. {kekurangan}")
                        print("Silahkan masukan ulang uang anda.")
                    else:
                        kembalian = uang_bayar - total_akhir
                        print(f"Terima kasih. Kembalian Anda: Rp. {kembalian}")
                        break
            
                except ValueError:
                    print("Input tidak valid. Silakan masukkan angka yang benar.")

        while True:
            pilihan = input("Apakah Anda ingin memesan ulang? (ya/tidak): ").lower()
            if pilihan == 'ya':
                total_makan = 0
                total_minum = 0
                pesan_makan = []
                pesan_minum = []
                clear_screen()
                break 
            elif pilihan == 'tidak':
                print("Terima kasih telah menggunakan layanan kami!")
                return 
            else:
                print("Pilihan tidak valid. Silakan jawab 'ya' atau 'tidak'.")
                
main()