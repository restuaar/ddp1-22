print("Selamat datang di program Mengenal Angkatan!")
print("===========================================")

print("Masukkan identitas mahasiswa: ")

# Inisiasi variabel awal
dict_of_nama = dict()
dict_of_npm = dict()

while True:
    query = input()
    if query == "STOP":
        print()
        break

    splitted_query = query.split(" ")
    nama = splitted_query[0]
    npm = splitted_query[1]
    bulan = splitted_query[4]

    if bulan not in dict_of_nama.keys():
        dict_of_nama[bulan] = {nama}
        dict_of_npm[bulan] = {npm}
    else:
        set_of_nama = dict_of_nama[bulan]
        set_of_nama.add(nama)
        set_of_npm = dict_of_npm[bulan]
        set_of_npm.add(npm)

while True:
    bulan = input("Cari mahasiswa berdasarkan bulan: ")
    if bulan == "STOP":
        break

    print("================= Hasil ================")
    if bulan not in dict_of_nama.keys():
        print(f"Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {bulan}.")
    else:
        print(f"Terdapat {len(dict_of_nama[bulan])} nama yang lahir di bulan {bulan}:")
        for nama in dict_of_nama[bulan]:
            print(f"- {nama}")

        print()
        print(f"Terdapat {len(dict_of_npm[bulan])} NPM yang lahir di bulan {bulan}:")
        for npm in dict_of_npm[bulan]:
            print(f"- {npm}")
    print()

print()
print("Terima kasih telah menggunakan program ini, semangat PMB-nya!")