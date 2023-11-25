# Restu Ahmad Ar Ridho
# NPM : 2206028951
# TP3

# FILE RECEIPT AKAN DI CETAK PADA FOLDER RECEIPT
# MENU DI CETAK SESUAI URUTAN PEMESANAN

# import libray yang diperlukan dalam mencetak receipt
from os import getcwd, chdir, listdir, mkdir

def menampilkan_menu(param:dict):
    """
    fungsi untuk menampilkan menu yang terdapat dalam dict
    """
    print("\nBerikut ini adalah menu yang kami sediakan:")
    for group_menu in param:
        print(group_menu + ":")
        for menu in param[group_menu]:
            print(f"{menu[0]} {menu[1]}, {convert_rp(menu[2])}")

def menampilkan_pesanan(param:dict) -> int:
    """
    fungsi untuk menampilkan pesanan dari pemesan dengan parameter dictionary
    dan mengembalikan harga total dari banyak yang dipesan berupa integer 
    """
    global menu_by_name_price

    total_harga = 0
    for menu in param:
        harga = param[menu] * menu_by_name_price[menu]
        total_harga += harga
        print(f"{menu} {param[menu]} buah, total {convert_rp(harga)}")
    if total_harga == 0: # kasus untuk user tidak memesan dianggap hanya menggunakan meja
        print("Belum terdapat pesanan.")
    return total_harga

def convert_rp(param:int) -> str:
    """
    fungsi untuk merubah tampilan harga yang berupa integer menjadi
    harga Rupiah dari parameter integer dan mengembalikan string
    """
    param_str = str(param)[::-1]
    temp = ""
    for i in range(0,len(param_str)):
        if i % 3 == 0 and i != 0:
            temp += "."
        temp += param_str[i]
    return "Rp" + temp[::-1]

# inisiasi variabel
MenuSalah = False # untuk validasi menu
menu = {} # menyimpan seluruh menu dari file menu.txt
menu_by_name_price = {} # menyimpan menu berdasarkan key nama dan value harga
menu_by_code_name = {} # menyimpan menu berdasarkan key kode dan value harga
# menyimpan pesanan
meja = {"1":"", "2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":"", "10":""} 
# menghubungkan no meja dengan nama pelanggan agar tidak terjadi duplikat
meja_customer = {"1":"", "2":"", "3":"", "4":"", "5":"", "6":"", "7":"", "8":"", "9":"", "10":""}

# VALIDASI MENU
with open("menu.txt") as file_open:
    print()
    current_group_menu = ""
    # membaca setiap line file menu
    for line in file_open:
        if line == "\n": # handle jika line kosong
            continue
        new_line = line.replace("\n","")
        # membagi kasus untuk nama group menu dan menu
        if new_line[:3] == "===" and new_line.count("=") == 3:
            if new_line[3:] in menu:
                current_group_menu = new_line[3:]
                continue
            menu[new_line[3:]] = []
            current_group_menu = new_line[3:]
        elif len(new_line.split(";")) == 3:
            temp = new_line.split(";")
            try: # menghandle kasus untuk harga tidak bilangan bulat dan bilangan bulat negatif
                harga = int(temp[2])
                if harga < 0:
                    MenuSalah = True
                    break
            except:
                MenuSalah = True
                break
            # kasus ketika menu sudah duplikat
            if (temp[0] in menu_by_code_name) or (temp[0] in menu_by_name_price):
                MenuSalah = True
                break
            if (temp[1] in menu_by_code_name) or (temp[1] in menu_by_name_price):
                MenuSalah = True
                break
            # menyimpan menu, nama dan harga, kode dan nama
            menu[current_group_menu] += [temp]
            menu_by_code_name[temp[0]] = temp[1]
            menu_by_name_price[temp[1]] = harga
        else:
            MenuSalah = True
            break

# membuat folder untuk receipt yang dicetak agar lebih rapih
if "receipt" not in listdir(getcwd()):
    mkdir("receipt")

meja_tujuan = ""
# PROGRAM UTAMA
while not MenuSalah:
    print("Selamat datang di Kafe Daun Daun Pacilkom")
    print("|- BUAT PESANAN\n|- UBAH PESANAN\n|- SELESAI MENGGUNAKAN MEJA")
    mode = input("Apa yang ingin anda lakukan? ")
    # membagi kasus pada setiap fitur yang diinput oleh user
    if mode == "BUAT PESANAN": # jika input "BUAT PESANAN"
        for no_meja in meja:
            # melakukan pengecekan meja
            if meja[no_meja] == "": # jika meja kosong
                nama_cus = input("Siapa nama anda? ")
                # inisiasi variabel sementara untuk menyimpan pesanan
                temp_pesanan = {}
                meja_customer[no_meja] = nama_cus # menyimpan nama ke meja

                menampilkan_menu(menu)
                
                menu_pesanan = input("\nMasukkan menu yang ingin Anda pesan: ")
                while menu_pesanan != "SELESAI":
                    # kasus untuk pesanan ada dalam menu
                    if (menu_pesanan in menu_by_code_name) or (menu_pesanan in menu_by_name_price):
                        if menu_pesanan in menu_by_code_name: # jika input merupakan kode
                            menu_pesanan = menu_by_code_name[menu_pesanan]
                        if menu_pesanan in temp_pesanan: # jika nama pesanan sudah dipesan
                            temp_pesanan[menu_pesanan] += 1
                            print(f"Berhasil memesan {menu_pesanan}.", end=" ") 
                        else:
                            temp_pesanan[menu_pesanan] = 1 # jika nama pesanan baru dipesan
                            print(f"Berhasil memesan {menu_pesanan}.", end=" ") 
                    else: # jika pesanan tidak terdapat dalam menu
                        print(f"Menu {menu_pesanan} tidak ditemukan.", end=" ")
                    menu_pesanan = input("Masukkan menu yang ingin Anda pesan: ")

                # menampilkan pesanan dan total harga
                print("\nBerikut adalah pesanan Anda:")
                total_harga = menampilkan_pesanan(temp_pesanan)
                print(f"\nTotal pesanan: {convert_rp(total_harga)}")

                # menyimpan pesanan
                meja[no_meja] = temp_pesanan
                if len(temp_pesanan) != 0: # kasus ketika user setidaknya memesan 1 menu
                    print(f"Pesanan akan kami proses,", end=" ")
                print(f"Anda bisa menggunakan meja nomor {no_meja}. Terima kasih.")
                break
            elif meja["10"] != "": # jika meja penuh
                print("Mohon maaf meja sudah penuh, silakan kembali nanti.")
                break
        
    elif mode == "UBAH PESANAN": # jika input "UBAH PESANAN"
        meja_tujuan = input("Nomor meja berapa? ")
        if (meja_tujuan in meja) and (meja[meja_tujuan] != ""): # jika input meja sesuai
            # iniasi variabel untuk dapat mengubah pesanan
            temp_pesanan = meja[meja_tujuan]

            # menampilkan menu dan pesanan sesuai dengan mejanya
            menampilkan_menu(menu)
            print("\nBerikut adalah pesanan Anda:")
            menampilkan_pesanan(temp_pesanan)
            print()

            while True:
                mode_ubah_pesanan = input("Apakah anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                if mode_ubah_pesanan == "GANTI JUMLAH": # jika input mode "GANTI JUMLAH"
                    target_menu = input("Menu apa yang ingin Anda ganti jumlahnya: ")
                    if (target_menu in menu_by_code_name): # jika input merupakan kode menu
                        target_menu = menu_by_code_name[target_menu]
                    if target_menu in temp_pesanan: # jika pesanan yang di input ada di pesanan sebelumnya
                        while True:
                            try: # handle untuk user menginput selain integer
                                jumlah_update_menu = int(input("Masukkan jumlah pesanan yang baru: "))
                                if jumlah_update_menu <= 0: # handle jika input user integer kurang dari 0
                                    print("Jumlah menu tidak sesuai!")
                                    continue
                                break
                            except ValueError:
                                print("Jumlah menu tidak sesuai!")
                        # melakukan update jumlah pesanan
                        temp_pesanan[target_menu] = jumlah_update_menu
                        print(f"Berhasil mengubah pesanan {target_menu} {jumlah_update_menu} buah.",end=" ")
                    else: # jika pesanan tidak terdapat pada pesanan sebelumnya
                        print(f"Menu {target_menu} tidak ditemukan!", end=" ")
                        
                elif mode_ubah_pesanan == "HAPUS": # jika mode input "HAPUS"
                    target_menu = input("Menu apa yang ingin Anda hapus dari pesanan: ")
                    if (target_menu in menu_by_code_name): # jika input merupakan kode menu
                        target_menu = menu_by_code_name[target_menu]
                    if target_menu in temp_pesanan: # jika pesanan yang di input ada di pesanan sebelumnya
                        jumlah_menu = temp_pesanan.pop(target_menu)
                        print(f"{jumlah_menu} buah {target_menu} dihapus dari pesanan.",end=" ")
                    else: # jika pesanan tidak terdapat pada pesanan sebelumnya
                        print(f"Menu {target_menu} tidak ditemukan!", end=" ")

                elif mode_ubah_pesanan == "TAMBAH PESANAN": # jika mode input "TAMBAH PESANAN"
                    target_menu = input("Masukkan menu yang ingin Anda pesan: ")
                    if (target_menu in menu_by_code_name): # jika input merupakan kode menu
                        target_menu = menu_by_code_name[target_menu]
                    if target_menu in temp_pesanan: # jika pesanan sudah ada di pesanan sebelumnnya
                        temp_pesanan[target_menu] += 1
                        print(f"Berhasil memesan {target_menu}.", end=" ")
                    elif target_menu in menu_by_name_price: # jika pesanan baru ditambahkan
                        temp_pesanan[target_menu] = 1
                        print(f"Berhasil memesan {target_menu}.", end=" ") 
                    else: # jika pesanan tidak terdapat pada menu
                        print(f"Menu {target_menu} tidak ditemukan!", end=" ")

                elif mode_ubah_pesanan == "SELESAI": # jika mode input "SELESAI"
                    # melakukan penyimpanan pesanan yang baru
                    meja[meja_tujuan] = temp_pesanan         
                    break

                else:
                    print("Fitur tidak valid. Coba lagi!", end=" ")
            # menampilkan pesanan dan total harga terbaru
            print("\nBerikut adalah pesanan terbaru Anda:")
            total_harga = menampilkan_pesanan(temp_pesanan)
            print(f"\nTotal pesanan: {convert_rp(total_harga)}")
        else: # kasus meja tidak sesuai
            print("Nomor meja kosong atau tidak sesuai!")

    elif mode == "SELESAI MENGGUNAKAN MEJA": # jika input "SELESAI MENGGUNAKAN MEJA"
        meja_tujuan = input("Nomor meja berapa? ")
        # melakukan pengecekan input no meja
        if (meja_tujuan in meja) and (meja[meja_tujuan] != ""): # jika sesuai
            # iniasi variabel untuk mendapatkan data pesanan
            nama_cus = meja_customer[meja_tujuan]
            temp_pesanan = meja[meja_tujuan]

            current_dir = getcwd() # variabel untuk kembali ke dir awal

            if len(temp_pesanan) != 0: # jika user setidaknya memesan 1 menu maka dicetak receipt
                chdir("./receipt") # mengganti dir

                name_file = f"receipt_{nama_cus}_{meja_tujuan}" # inisiasi nama file
                # mencetak pesanan kedalam file receipt
                with open(name_file,"w") as write_file:
                    total_harga = 0
                    for pesanan in temp_pesanan: # untuk mendapatkan kode makanan
                        for i in menu_by_code_name:
                            if menu_by_code_name[i] == pesanan:
                                code_menu = i
                        # menghitung harga, jumlah, dan total harga dari setiap menu yang dipesan
                        banyak_menu = temp_pesanan[pesanan]
                        harga_menu = menu_by_name_price[pesanan]
                        total_harga_menu = harga_menu * banyak_menu
                        total_harga += total_harga_menu
                        # menulis kedalam file yang dituju
                        write_file.write(f"{code_menu};{pesanan};{banyak_menu};{harga_menu};{total_harga_menu}\n")
                    write_file.write(f"\nTotal {total_harga}")

                chdir(current_dir) # mengembalikan ke dir awal 

            # membersihkan data dari pesanan yang sudah di cetak di receipt
            meja[meja_tujuan] = ""
            meja_customer[meja_tujuan] = ""
            print(f"Pelanggan atas nama {nama_cus} selesai menggunakan meja {meja_tujuan}.")
        else: # jika input no meja tidak sesuai
            print("Nomor meja kosong atau tidak sesuai!")

    elif mode == "SELESAI": # untuk Pak Bambang nutup programnnya
        temp_lst = []
        for no_meja in meja_customer:
            if meja_customer[no_meja] != "":
                temp_lst.append(meja_customer[no_meja])
        if len(temp_lst) == 0:
            break
        else:
            print("Selesaikan pesanan terlebih dahulu dengan nama",end=" ")
            for i in range(len(temp_lst)):
                if temp_lst[i] == temp_lst[-1]:
                    print(temp_lst[i], end=".")
                    continue
                print(temp_lst[i], end=", ")

    else: # jika input selain "BUAT PESANAN" , "UBAH PESANAN", "SELESAI MENGGUNAKAN MEJA"
        print("Fitur tidak valid. Coba lagi!")
    print("\n---")

else: # jika menu tidak valid
    print("Daftar menu tidak valid, cek kembali menu.txt!")

print("\nTerima kasih sudah menggunakan progam ini.")