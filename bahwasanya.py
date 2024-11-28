import os
import datetime
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_invoice():
    return f"INV/{datetime.datetime.now().strftime('%Y%m%d')}/{random.randint(1000,9999)}"

def makanan():
    global total_makan, pesan_makan, jumlah_porsi
    total_makan = 0
    pesan_makan = []

    while True:
        print("-------------------------------------------------------------")
        print("             : pilih menu makanan :          ")
        print("-------------------------------------------------------------")
        print("1.  Nasi Goreng Kampung                Rp. 18.000")
        print("2.  Nasi Goreng Spesial                Rp. 20.000")
        print("3.  Indomie Polos                      Rp. 8.000")
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
        print("-------------------------------------------------------------")
        
        try:
            menu_makanan = int(input("Silahkan pilih menu, masukan angka 0 untuk selesai: "))
            if menu_makanan == 0:
                break
            
            if menu_makanan not in range (1, 16):
                print("Pilihan tidak tersedia. Silakan pilih menu yang benar.")
                continue

            jumlah_porsi = int(input("Masukan Berapa porsi: "))
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
        print("-------------------------------------------------------------")
        print("             : pilih menu minuman :          ")
        print("-------------------------------------------------------------")
        print("1.  Es Teh Maniez                      Rp. 5.000")
        print("2.  Lemon Tea                          Rp. 8.000")
        print("3.  Teh Tarik                          Rp. 10.000")
        print("4.  Bubble Milk Tea                    Rp. 15.000")
        print("5.  Americano                          Rp. 8.000")
        print("6.  Kopi Tubruk                        Rp. 8.000")
        print("7.  Latte                              Rp. 15000")
        print("8.  Cappucino                          Rp. 12.000")
        print("9.  Hot Chocolatte                     Rp. 10.000")
        print("10. Matcha                             Rp. 10.000")
        print("11. Fresh Juice                        Rp. 12.000")
        print("12. Jeruk Peras                        Rp. 10.000")
        print("13. Susu Jahe                          Rp. 10.000")
        print("14. Soda Gembira                       Rp. 12.000")
        print("15. Air Mineral                        Rp. 5.000")
        print("0.  Untuk selesai memesan minuman               ")
        print("-------------------------------------------------------------")
        
        try:
            menu_minuman = int(input("Silahkan pilih menu, masukan angka 0 untuk selesai: "))
            if menu_minuman == 0:
                break
            
            if menu_minuman not in range (1, 16):
                print("Maaf menu tidak tersedia. Silakan pilih menu yang benar.")
                continue

            jumlah_gelas = int(input("Masukan Berapa gelas: "))
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


def simpan_ke_file(nama_file, pesan_makan, pesan_minum, total, diskon=0):
    with open(nama_file, 'a') as file:
        file.write("=====================================================================================================================================================================================\n")
        file.write("\n")
        file.write("\n")
        file.write("=====================================================================================================================================================================================\n")
        invoice_number = generate_invoice()
        file.write("\n===================================================\n")
        file.write(f"Invoice: {invoice_number}\n")
        file.write("===================================================\n")
        file.write("                DETAIL PEMBELIAN                       \n")
        file.write("===================================================\n")
        file.write("MAKANAN:\n")
        for item in pesan_makan:
            file.write(f"- {item[0]} x{item[1]} = Rp. {item[2]}\n")
        file.write("\nMINUMAN:\n")
        for item in pesan_minum:
            file.write(f"- {item[0]} x{item[1]} = Rp. {item[2]}\n")
        file.write("\n===================================================\n")
        file.write(f"Total Sebelum Diskon : Rp. {total + diskon}\n")
        file.write(f"Diskon               : Rp. {diskon}\n")
        file.write(f"Total Akhir          : Rp. {total}\n")
        file.write(f"Waktu Transaksi      : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write("===================================================\n")
        file.write("=====================================================================================================================================================================================\n")
        file.write("\n")
        file.write("\n")
        file.write("=====================================================================================================================================================================================\n")

    
    print(f"Transaksi berhasil disimpan di {nama_file}")


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

        jumlah_semua = total_makan + total_minum
        jumlah_semua = promo(jumlah_semua)

        print("-------------------------------------------------------")
        print("                Daftar Pembelian                       ")
        print("-------------------------------------------------------")
        for item in pesan_makan:
            print(f" Makanan : {item[0]}                               ")
            print(f" Porsi   : {item[1]}                                 ")
        print("-------------------------------------------------------")
        for item in pesan_minum:
            print(f" Minuman : {item[0]}                               ")
            print(f" Gelas   : {item[1]}                                 ")
        print("-------------------------------------------------------")
        print(f"Tanggal  : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-------------------------------------------------------")
        print(f" Total yang harus dibayar : Rp. {jumlah_semua}             ")
        print("-------------------------------------------------------")

        # Hitung diskon (jika ada)
        diskon_total = total_makan + total_minum - jumlah_semua if jumlah_semua < (total_makan + total_minum) else 0
        simpan_ke_file('daftar_pembelian.txt', pesan_makan, pesan_minum, jumlah_semua, diskon_total)
        

        while True:
            try:
                uang_bayar = int(input("Masukan uang anda: Rp. "))
                if uang_bayar < jumlah_semua:
                    kekurangan = jumlah_semua - uang_bayar
                    print(f"Maaf, uang Anda kurang Rp. {kekurangan}")
                    print("Silahkan bayar kembali sejumlah yang kurang")
                else:
                    kembalian = uang_bayar - jumlah_semua
                    print(f"Terima kasih. Kembalian Anda: Rp. {kembalian}")
                    break
            
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka yang benar.")
                clear_screen()

        while True:
            pilihan = input("Apakah Anda ingin memesan ulang? (ya/tidak): ").lower()
            if pilihan == 'ya':
                total_makan = 0
                total_minum = 0
                pesan_makan = []
                pesan_minum = []
                print("\n--- Pemesanan Baru ---")
                clear_screen()
                break 
            elif pilihan == 'tidak':
                print("Terima kasih telah menggunakan layanan kami!")
                return 
            else:
                print("Pilihan tidak valid. Silakan jawab 'ya' atau 'tidak'.")
                clear_screen()
                
main()