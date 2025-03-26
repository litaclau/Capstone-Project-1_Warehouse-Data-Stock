# Capstone Project Module 1 Purwadhika -
# nama_barang       : Solita Claudya A
# Program           : JCDSOL-019


inventory = [
    {"kode": "A01", "nama_barang": "Kemeja", "jenis": "Atasan", "stok": 100, "lokasi_rak": "RA01"},
    {"kode": "A02", "nama_barang": "Kaos", "jenis": "Atasan", "stok": 250, "lokasi_rak": "RA02"},
    {"kode": "A03", "nama_barang": "Jaket", "jenis": "Atasan", "stok": 80, "lokasi_rak": "RA03"},
    
    {"kode": "B01", "nama_barang": "Celana", "jenis": "Bawahan", "stok": 320, "lokasi_rak": "RB01"},
    {"kode": "B02", "nama_barang": "Jeans", "jenis": "Bawahan", "stok": 150, "lokasi_rak": "RB02"},
    
    {"kode": "C01", "nama_barang": "Dress", "jenis": "Setelan", "stok": 50, "lokasi_rak": "RC01"},
    {"kode": "C02", "nama_barang": "Jumpsuit", "jenis": "Setelan", "stok": 80, "lokasi_rak": "RC02"},
]


def menu1_lihat_data():
    while True:
        print("\n========== Melihat Data Gudang ==========")
        print("1. Menampilkan Semua Data")  
        print("2. Menampilkan Data Berdasarkan Jenis")  
        print("3. Kembali ke Menu Utama")  

        sub_pilihan = input("\nSilakan Pilih [1-3]: ")

        if sub_pilihan == '1':  
            submenu1_1_lihatsemua_data()
        elif sub_pilihan == '2':  
            submenu1_2_lihatberdasarkan_jenis()
        elif sub_pilihan == '3': 
            print("\nKembali ke Menu Utama...\n")
            break
        else:
            print("\n>>>>> Pilihan yang Anda Masukkan Salah <<<<<")


def submenu1_1_lihatsemua_data():
    print("-----------------------------------------------------------------")
    print("Kode\tNama Barang    \tJenis     \tStok (pcs)\tLokasi Rak")
    print("-----------------------------------------------------------------")

    for data in inventory:
        print(f"{data['kode']}\t{data['nama_barang']:15}\t{data['jenis']:10}\t{data['stok']:9}\t{data['lokasi_rak']}")
    print("-----------------------------------------------------------------")



def submenu1_2_lihatberdasarkan_jenis():
    while True:
        print("\n========== CARI BARANG BERDASARKAN JENIS ==========")
        print("**Ketik 'batal' untuk membatalkan proses")

        jenis_dicari = input("\nMasukkan Jenis Barang (Atasan/Bawahan/Setelan): ").capitalize()

        if jenis_dicari.lower() == 'batal':  
            print("\nKembali ke menu sebelumnya...\n")
            break  

        
        for data in inventory:
            if data['jenis'].lower() == jenis_dicari.lower():
                break  
        else:
            print("\n>>>>>  Tidak Ada Barang dengan Jenis Tersebut  <<<<<")
            break  

      
        print("\n--------------------------------------------------------")
        print("Kode\tNama Barang    \tStok (pcs)\tLokasi Rak")
        print("--------------------------------------------------------")

        for data in inventory:
            if data['jenis'].lower() == jenis_dicari.lower():
                print(f"{data['kode']}\t{data['nama_barang']:15}\t{data['stok']:9}\t{data['lokasi_rak']}")

        print("--------------------------------------------------------")
        break 



def menu2_tambah_data():
    while True:
        print("\n========== MENAMBAH DATA GUDANG ==========\n")
        submenu1_1_lihatsemua_data()
        print("**Ketik 'batal' untuk membatalkan proses\n")

        while True:
            kode_barang = input("Masukkan Kode Barang: ").upper()
            if kode_barang.lower() == "batal":
                print("\n>>>>>  Proses Dibatalkan. Kembali ke Menu Utama.  <<<<<")
                return

            if any(item["kode"] == kode_barang for item in inventory):
                print("\n>>>>>  Kode barang sudah ada! Harap masukkan kode lain.  <<<<<")
            else:
                break

        while True:
            nama_barang = input("Masukkan Nama Barang: ").capitalize()
            if nama_barang.lower() == "batal":
                print("\n>>>>>  Proses Dibatalkan. Kembali ke Menu Utama.  <<<<<")
                return

            if any(item["nama_barang"].lower() == nama_barang.lower() for item in inventory):
                print("\n>>>>>  Nama barang sudah ada! Harap masukkan nama lain.  <<<<<")
            else:
                break

        jenis = input("Masukkan Jenis Barang: ").capitalize()
        if jenis.lower() == "batal":
            print("\n>>>>>  Proses Dibatalkan. Kembali ke Menu Utama.  <<<<<")
            return

        while True:
            jumlah_input = input("Masukkan Jumlah Stok Barang: ")
            if jumlah_input.lower() == "batal":
                print("\n>>>>>  Proses Dibatalkan. Kembali ke Menu Utama.  <<<<<")
                return
            if jumlah_input.isdigit() and int(jumlah_input) > 0:
                jumlah = int(jumlah_input)
                break
            print("\n>>>>>  Harap Masukkan Angka yang Valid!  <<<<<")

        lokasi_rak = input("Masukkan Lokasi Rak: ").upper()
        if lokasi_rak.lower() == "batal":
            print("\n>>>>>  Proses Dibatalkan. Kembali ke Menu Utama.  <<<<<")
            return

        while True:
            konfirmasi = input("\nApakah Anda yakin ingin menambahkan data ini? (yes/no): ").lower()
            if konfirmasi == "yes":
                inventory.append({
                    "kode": kode_barang,
                    "nama_barang": nama_barang,
                    "jenis": jenis,
                    "stok": jumlah,
                    "lokasi_rak": lokasi_rak
                })
                print(f"\n>>>>>  Barang '{nama_barang}' Berhasil Ditambahkan!  <<<<<")
                return
            elif konfirmasi == "no":
                print("\n>>>>>  Proses dibatalkan. Kembali ke awal input.  <<<<<")
                break
            else:
                print("\n>>>>>  Harap masukkan 'yes' atau 'no'.  <<<<<")



def menu3_ubah_data():
    while True:
        print("\n========== MENGUBAH DATA GUDANG ==========\n")
        submenu1_1_lihatsemua_data()
       
        print("**Ketik 'batal' untuk membatalkan proses\n")        
        kode_barang = input("Masukkan Kode Barang yang Ingin Diubah: ").upper()
        
        if kode_barang.lower() == "batal":
            print("\n>>>>>  Proses Dibatalkan. Kembali ke Menu Utama.  <<<<<")
            break

        for data in inventory:
            if data["kode"] == kode_barang:
                print("\n>>>>>  Barang Ditemukan!  <<<<<")
                print(f"Kode: {data['kode']}, Nama: {data['nama_barang']}, Jenis: {data['jenis']}, Stok: {data['stok']}, Lokasi: {data['lokasi_rak']}")

                nama_barang = input("Masukkan Nama Barang Baru (Tekan Enter jika tidak ingin mengubah): ").capitalize()
                jenis = input("Masukkan Jenis Baru (Tekan Enter jika tidak ingin mengubah): ").capitalize()
                lokasi_rak = input("Masukkan Lokasi Rak Baru (Tekan Enter jika tidak ingin mengubah): ").upper()

                while True:
                    stok_input = input("Masukkan Stok Baru (kosongkan jika tidak ingin mengubah): ")
                    if stok_input == "":
                        break
                    if stok_input.isdigit() and int(stok_input) >= 0:
                        stok_baru = int(stok_input)
                        break
                    print("\n>>>>>  Harap Masukkan Angka yang Valid!  <<<<<")

                while True:
                    konfirmasi = input("\nApakah Anda yakin ingin mengubah data ini? (yes/no): ").lower()
                    if konfirmasi == "yes":
                        if nama_barang:
                            data["nama_barang"] = nama_barang
                        if jenis:
                            data["jenis"] = jenis
                        if lokasi_rak:
                            data["lokasi_rak"] = lokasi_rak
                        if stok_input:
                            data["stok"] = stok_baru

                        print("\n>>>>>  Data Berhasil Diperbarui!  <<<<<")
                        return
                    elif konfirmasi == "no":
                        print("\n>>>>>  Perubahan Dibatalkan. Kembali ke awal input.  <<<<<")
                        return
                    else:
                        print("\n>>>>>  Harap masukkan 'yes' atau 'no'.  <<<<<")

        print("\n>>>>>  Kode Barang Tidak Ditemukan!  <<<<<")
        


def menu4_hapus_data():
    while True:
        print("\n========== MENGHAPUS DATA GUDANG ==========\n")
        submenu1_1_lihatsemua_data()
        print("**Ketik 'batal' untuk membatalkan proses\n")
        
        kode_barang = input("Masukkan Kode Barang yang Ingin Dihapus: ").upper()

        if kode_barang.lower() == "batal":
            print("\n>>>>>  Proses Dibatalkan. Kembali ke Menu Utama.  <<<<<")
            break

        for data in inventory:
            if data["kode"] == kode_barang:
                while True: 

                    konfirmasi = input("\nApakah Anda yakin ingin menghapus data ini? (yes/no): ").lower()
                    if konfirmasi == "yes":
                        inventory.remove(data)
                        print(f"\n>>>>>  Barang '{data['nama_barang']}' Berhasil Dihapus!  <<<<<")
                        return  
                    elif konfirmasi == "no":
                        print("\n>>>>>  Penghapusan Dibatalkan. Kembali ke awal input.  <<<<<")
                        break 
                    else:
                        print("\n>>>>>  Harap masukkan 'yes' atau 'no'.  <<<<<")

                break

        else:
            print("\n>>>>>  Kode Barang Tidak Ditemukan!  <<<<<")




while True:
    print("\n========== GUDANG LTS FASHION ==========")
    print("1. Melihat Data Gudang")  
    print("2. Menambah Data Gudang")  
    print("3. Mengubah Data Gudang")  
    print("4. Menghapus Data Gudang")  
    print("5. Keluar")  

    pilihan = input("\nSilakan Pilih [1-5]: ")

    if pilihan == '1':
        menu1_lihat_data()

    elif pilihan == '2':
        menu2_tambah_data()

    elif pilihan == '3':
        menu3_ubah_data()
    
    elif pilihan == '4':
        menu4_hapus_data()
    
    elif pilihan == '5':
        print("\n>>>>>  Keluar dari Program  <<<<<\n")
        break  
    
    else:
        print("\n>>>>>  Pilihan yang Anda Masukkan Salah  <<<<<")
