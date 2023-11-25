import math

# meminta input pengguna
nama = input("Nama: ")
panjang_persegi = float(input("Panjang persegi nametag (cm): "))
panjang_trapesium = float(input("Panjang trapesium nametag (cm): "))
banyak_nametag = int(input("Banyak nametag: "))

# menghitung luas setiap bangun datar
luas_persegi = panjang_persegi * panjang_persegi
luas_segitiga = panjang_persegi * panjang_persegi / 2
luas_setengah_lingkaran = math.pi * panjang_persegi * panjang_persegi / 8
luas_trapesium = (panjang_persegi + panjang_trapesium) * panjang_persegi / 2

# menghitung luas nametag
luas_satu_nametag = luas_persegi + luas_segitiga + \
    luas_setengah_lingkaran + luas_trapesium
luas_total_nametag = luas_satu_nametag * banyak_nametag

# menghitung total biaya
total_biaya = math.ceil(luas_total_nametag * 0.40 / 1000) * 1000

# mencetak hasil
print("\nHalo, {0}! Berikut informasi terkait nametag kamu:\n".format(nama))
print("Luas 1 nametag: {0:.2f} cm^2".format(luas_satu_nametag))
print("Luas total nametag: {0:.2f} cm^2".format(luas_total_nametag))
print("Uang yang diperlukan: Rp" + str(total_biaya))
