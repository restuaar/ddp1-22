
print("Selamat datang di Pacil Mart!\n")
file_input = input("Masukkan nama file input: ")

try:
    with open(file_input, 'r') as file:
        lines = file.readlines()

    # cek apakah file kosong
    if len(lines) == 0:
        print("File input ada tapi kosong")
    
    else:
        print("""Berikut adalah daftar belanjaanmu:""")
        print()
        print("Nama Barang |  Jumlah| Kembalian")
        print("—-------------------------------")

        jumlah_dibeli = 0
        with open(file_input, 'r') as file:

            for line in file:
                word = line.split()
                nama_barang = word[0]
                uang_bayar = int(word[1])
                harga = int(word[2])

                #Menghitung jumlah barang yang dibeli dan kembalian uangnya
                jumlah = int(uang_bayar/harga)
                kembalian = int(uang_bayar % harga)

                print(f"{nama_barang:<12s}|{jumlah:>8d}|{kembalian:>10d}")
            print()
            print("Terima kasih sudah belanja di Pacil Mart!")

except FileNotFoundError:
    print("File tidak tersedia")