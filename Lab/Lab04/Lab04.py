# Restu Ahmad Ar Ridho
# NPM : 2206028951
# Lab04

print("Selamat datang di Pacil Mart!\n")

# Meminta input nama file dari user
nama_file_input = input("Masukkan nama file input: ")

# Membagi kasus jika file ada dan tidak ada
try:
    with open(nama_file_input,"r") as file_input:
        baris = file_input.readlines()
except:
    # Ketika file tidak ada mencetak output dan keluar program
    print("File tidak tersedia")
    exit()

# Jika file ada namun kosong maka mencetak output dan keluar program
if len(baris) == 0:
    print("File input ada tapi kosong.")
    exit()

# Mencetak judul
print("Berikut adalah daftar belanjaanmu:\n")
print(f"{'Nama Barang':<12}|{'Jumlah':>8}|{'Kembalian':>10}")
print("-"*32)

# Melakakukan perulangan pada setiap baris
for tiap_baris in baris:

    # Deklarasi variabel sementara untuk setiap kata pada baris dan mengoperasikannya
    temp_nama_barang = ""
    temp_uang_alokasi = 0
    temp_harga_barang = 0

    # Mengubah 1 baris menjadi perkata
    tiap_kata = tiap_baris.split()

    # Menambahkan ke temp variabel
    temp_nama_barang += tiap_kata[0]
    temp_uang_alokasi += int(tiap_kata[1])
    temp_harga_barang += int(tiap_kata[2])

    # Menghitung jumlah barang dan kembalian
    jumlah = int(temp_uang_alokasi)//int(temp_harga_barang)
    kembalian = int(temp_uang_alokasi) - (int(temp_harga_barang)*jumlah)
    
    # Mencetak perbaris
    print(f"{temp_nama_barang:<12}|{jumlah:>8}|{kembalian:>10}")

print("\nTerima kasih sudah belanja di Pacil Mart!")