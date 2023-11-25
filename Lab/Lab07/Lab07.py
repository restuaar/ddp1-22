# Restu Ahmad Ar Ridho
# NPM : 2206028951
# Lab 07

print("Selamat datang di program Mengenal Angkatan")
print("===========================================")

# deklarasi variabel dictionary dengan value bulan dan key nama dan npm
dict_nama_bulan = {}
dict_npm_bulan = {}

# meminta input dari user
identitas = input("Masukkan identitas mahasiswa: \n")
while identitas != "STOP": # melakukan pengulangan sampai input STOP
    temp_lst_identitas = identitas.split()
    # menambahkan input user kedalam dictionary
    # key = nama dan value bulan
    dict_nama_bulan[temp_lst_identitas[0].casefold().capitalize()] = temp_lst_identitas[4]
    # key = npm dan value bulan
    dict_npm_bulan[temp_lst_identitas[1]] = temp_lst_identitas[4]
    identitas = input()
print()

# deklarasi variabel untuk pengulangan
isLanjut = True
while isLanjut: # melakukan pengulangan
    temp_lst_mahasiswa = []

    # meminta input user
    cari_bulan_mahasiswa = input("Cari mahasiswa berdasarkan bulan: ")

    # membagi kasus jika input "STOP"
    if cari_bulan_mahasiswa != "STOP":
        print("================= Hasil ================")
        # deklarasi variabel untuk menghitung banyak nama
        count_nama = 0

        # melakukan pengecekan terhadap value dictionary
        for i in dict_nama_bulan:
            if dict_nama_bulan[i] == cari_bulan_mahasiswa:
                count_nama += 1
                temp_lst_mahasiswa.append(i) # jika sama maka ditambahkan kedalam sebuah list
        if count_nama > 0: # jika terdapat maka dicetak di terminal
            print(f"Terdapat {count_nama} nama yang lahir di bulan {cari_bulan_mahasiswa}:")
            for j in temp_lst_mahasiswa:
                print(f"- {j}")
            print()

        temp_lst_mahasiswa.clear() # menghapus list untuk menyimpan nama
        # deklarasi variabel untuk menghitung banyak npm
        count_npm = 0

        # melakukan pengecekan terhadap value dictionary untuk npm
        for i in dict_npm_bulan:
            if dict_npm_bulan[i] == cari_bulan_mahasiswa:
                count_npm += 1
                temp_lst_mahasiswa.append(i) # jika sama maka ditambahkan kedalam list
        if count_npm > 0: # jika ada maka dicetak di terminal
            print(f"Terdapat {count_npm} NPM yang lahir di bulan {cari_bulan_mahasiswa}:")
            for j in temp_lst_mahasiswa:
                print(f"- {j}")

        # jika tidak ada yang cocok dalam npm
        if count_nama == 0 and count_npm == 0:
            print(f"Tidak ditemukan mahasiswa dan NPM yang lahir di bulan {cari_bulan_mahasiswa}.")
        print() 
    
    # jika input "STOP"
    else:
        isLanjut = False
        break

print()
print("Terima kasih telah menggunakan program ini, semangat PMB-nya!")
    
