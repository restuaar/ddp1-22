# Contoh Solusi Tugas Pemrograman 3 DDP1 2022 (versi dosen)
# Author: Ichlasul Affan (IAF)
# Disclaimer: untuk output tidak harus sepenuhnya sama persis dengan yang ada di soal,
#             boleh saja jika ada yang sedikit berbeda, yang penting datanya lengkap dan benar.
# Waktu pengerjaan (IAF): 1 jam 48 menit (stopwatched)

def read_menu():
    with open("menu.txt", "r") as berkas_menu:
        daftar_kategori = set()
        daftar_menu = {}
        daftar_nama_menu = []
        try:
            kategori = ""
            for raw_menu in berkas_menu:
                if raw_menu.startswith("==="):
                    kategori = raw_menu.strip().replace("===", "")
                    daftar_kategori.add(kategori)
                else:
                    kode_menu, nama_menu, harga_raw = raw_menu.strip().split(";")
                    harga = int(harga_raw)
                    if harga < 0:
                        print("Daftar menu tidak valid, cek kembali menu.txt!")
                        return None
                    if kode_menu not in daftar_nama_menu and nama_menu not in daftar_nama_menu:
                        daftar_menu[kode_menu] = (nama_menu, harga, kategori)
                        daftar_nama_menu.extend(kode_menu, nama_menu)
                    else:
                        print("Daftar menu tidak valid, cek kembali menu.txt!")
                        return None
        except (ValueError, IndexError):
            print("Daftar menu tidak valid, cek kembali menu.txt!")
            return None
        return daftar_kategori, daftar_menu

def cetak_daftar_menu(daftar_kategori, daftar_menu):
    print("\nBerikut ini adalah menu yang kami sediakan:")
    daftar_string_menu = {kategori: [] for kategori in daftar_kategori}
    for kode_menu, menu in daftar_menu.items():
        nama_menu, harga_satuan, kategori = menu
        daftar_string_menu[kategori].append(f"{kode_menu} {nama_menu}, Rp{harga_satuan:,d}")
    for kategori in daftar_string_menu:
        print(f"{kategori}:")
        for string_menu in daftar_string_menu[kategori]:
            print(string_menu)

def ambil_menu(daftar_menu, nama_menu_pesanan):
    if nama_menu_pesanan in daftar_menu:
        return nama_menu_pesanan, daftar_menu[nama_menu_pesanan]
    else:
        for kode_menu, menu in daftar_menu.items():
            if menu[0] == nama_menu_pesanan:
                return kode_menu, menu
    return None

def buat_pesanan(daftar_menu):
    daftar_pesanan = {}
    pesanan = input("\nMasukkan menu yang ingin Anda pesan: ")
    while pesanan != "SELESAI":
        tambah_pesanan(daftar_menu, daftar_pesanan, pesanan)
        pesanan = input("Masukkan menu yang ingin Anda pesan: ")
    return daftar_pesanan

def cetak_pesanan(daftar_menu, daftar_pesanan):
    print("\nBerikut adalah pesanan Anda: ")
    harga_keseluruhan = 0
    for kode_menu in daftar_pesanan:
        menu = daftar_menu[kode_menu]
        nama_menu = menu[0]
        harga_satuan = menu[1]
        jumlah_pesanan = daftar_pesanan[kode_menu]
        harga_total = harga_satuan * jumlah_pesanan
        harga_keseluruhan += harga_total
        print(f"{nama_menu} {jumlah_pesanan} buah, total Rp{harga_total:,d}")
    print(f"\nTotal pesanan: Rp{harga_keseluruhan:,d}")

def reservasi_meja(daftar_meja, nama_pelanggan, daftar_pesanan):
    for i in range(10):
        if daftar_meja[i] == None:
            daftar_meja[i] = (nama_pelanggan, daftar_pesanan)
            return i + 1
    return None

def ambil_data_pelanggan(daftar_meja, nomor_meja_raw):
    try:
        nomor_meja = int(nomor_meja_raw) - 1
        data_pelanggan = daftar_meja[nomor_meja]
        if data_pelanggan is None:
            print("Nomor meja kosong atau tidak sesuai!")
        return data_pelanggan
    except (ValueError, IndexError):
        print("Nomor meja kosong atau tidak sesuai!")
        return None

def ganti_jumlah_pesanan(daftar_menu, daftar_pesanan, pesanan):
    menu_raw = ambil_menu(daftar_menu, pesanan)
    if menu_raw is None:
        print(f"Menu {pesanan} tidak ditemukan.", end=" ")
    else:
        kode_menu, menu = menu_raw
        if kode_menu not in daftar_pesanan:
            print(f"Menu {pesanan} tidak Anda pesan sebelumnya.", end=" ")
        else:
            try:
                jumlah_baru = int(input("Masukkan jumlah pesanan yang baru: "))
                if jumlah_baru <= 0:
                    print(f"Jumlah harus bilangan positif!", end=" ")
                else:
                    daftar_pesanan[kode_menu] = jumlah_baru
                    print(f"Berhasil mengubah pesanan {menu[0]} {jumlah_baru} buah.", end=" ")
            except ValueError:
                print(f"Jumlah harus bilangan positif!", end=" ")

def hapus_pesanan(daftar_menu, daftar_pesanan, pesanan):
    menu_raw = ambil_menu(daftar_menu, pesanan)
    if menu_raw is None:
        print(f"Menu {pesanan} tidak ditemukan.", end=" ")
    else:
        kode_menu, menu = menu_raw
        if kode_menu not in daftar_pesanan:
            print(f"Menu {pesanan} tidak Anda pesan sebelumnya.", end=" ")
        else:
            jumlah_pesanan_terhapus = daftar_pesanan.pop(kode_menu)
            print(f"{jumlah_pesanan_terhapus} buah {menu[0]} dihapus dari pesanan.", end=" ")

def tambah_pesanan(daftar_menu, daftar_pesanan, pesanan):
    menu_raw = ambil_menu(daftar_menu, pesanan)
    if menu_raw is None:
        print(f"Menu {pesanan} tidak ditemukan.", end=" ")
    else:
        kode_menu, menu = menu_raw
        if kode_menu not in daftar_pesanan:
            daftar_pesanan[kode_menu] = 0
        daftar_pesanan[kode_menu] += 1
        print(f"Berhasil memesan {menu[0]}.", end=" ")

def hapus_pelanggan_dari_meja(daftar_meja, nomor_meja_raw):
    try:
        nomor_meja = int(nomor_meja_raw) - 1
        data_pelanggan = daftar_meja[nomor_meja]
        if data_pelanggan is None:
            print("Nomor meja kosong atau tidak sesuai!")
        else:
            daftar_meja[nomor_meja] = None
            print(f"Pelanggan atas nama {data_pelanggan[0]} selesai menggunakan meja {nomor_meja_raw}.")
        return data_pelanggan
    except (ValueError, IndexError):
        print("Nomor meja kosong atau tidak sesuai!")
        return None

def cetak_receipt(daftar_menu, data_pelanggan):
    nama_pelanggan, daftar_pesanan = data_pelanggan
    with open(f"receipt_{nama_pelanggan}.txt", "w") as receipt:
        harga_keseluruhan = 0
        for kode_menu in daftar_pesanan:
            menu = daftar_menu[kode_menu]
            nama_menu = menu[0]
            harga_satuan = menu[1]
            jumlah_pesanan = daftar_pesanan[kode_menu]
            harga_total = harga_satuan * jumlah_pesanan
            harga_keseluruhan += harga_total
            print(f"{kode_menu};{nama_menu};{jumlah_pesanan};{harga_satuan};{harga_total}", file=receipt)
        print(f"\nTotal {harga_keseluruhan}", file=receipt)

daftar_kategori, daftar_menu = read_menu()
if not daftar_menu:
    exit()
daftar_meja = [None for _ in range(10)]

while True:
    print("Selamat datang di Kafe Daun Daun Pacilkom")
    command = input("Apa yang ingin anda lakukan? ")
    if command == "BUAT PESANAN":
        if None not in daftar_meja:
            print("Mohon maaf meja sudah penuh, silakan kembali nanti.")
        else:
            nama_pelanggan = input("Siapa nama anda? ")
            cetak_daftar_menu(daftar_kategori, daftar_menu)
            daftar_pesanan = buat_pesanan(daftar_menu)
            cetak_pesanan(daftar_menu, daftar_pesanan)
            nomor_meja = reservasi_meja(daftar_meja, nama_pelanggan, daftar_pesanan)
            print(f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {nomor_meja}. Terima kasih.")
    elif command == "UBAH PESANAN":
        nomor_meja = input("Nomor meja berapa? ")
        data_pelanggan = ambil_data_pelanggan(daftar_meja, nomor_meja)
        if data_pelanggan is not None:
            daftar_pesanan = data_pelanggan[1]
            cetak_daftar_menu(daftar_kategori, daftar_menu)
            cetak_pesanan(daftar_menu, daftar_pesanan)
            subcommand = input("\nApakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            while subcommand != "SELESAI":
                if subcommand == "GANTI JUMLAH":
                    nama_pesanan = input("Menu apa yang ingin Anda ganti jumlahnya: ")
                    ganti_jumlah_pesanan(daftar_menu, daftar_pesanan, nama_pesanan)
                elif subcommand == "HAPUS":
                    nama_pesanan = input("Menu apa yang ingin Anda hapus dari pesanan: ")
                    hapus_pesanan(daftar_menu, daftar_pesanan, nama_pesanan)
                elif subcommand == "TAMBAH PESANAN":
                    pesanan_baru = input("Masukkan menu yang ingin Anda pesan: ")
                    tambah_pesanan(daftar_menu, daftar_pesanan, pesanan_baru)
                subcommand = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            cetak_pesanan(daftar_menu, daftar_pesanan)
    elif command == "SELESAI MENGGUNAKAN MEJA":
        nomor_meja = input("Nomor meja berapa? ")
        data_pelanggan = hapus_pelanggan_dari_meja(daftar_meja, nomor_meja)
        if data_pelanggan is not None:
            cetak_receipt(daftar_menu, data_pelanggan)

    print("\n---")
