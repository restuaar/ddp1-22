# Restu Ahmad Ar Ridho
# NPM : 2206028951

# menggunakan modul math untuk mengambil nilai pi
import math

# meminta user meng-input nilai yang diinginkan
nama = input("Nama: ")
panjang_persegi = float(input("Panjang persegi nametag (cm): "))
panjang_trapesium = float(input("Panjang trapesium nametag (cm): "))
banyak_nametag = int(input("Banyak nametag: "))

# menghitung luas persegi
luas_persegi = panjang_persegi * panjang_persegi

# menghitung luas segitiga
luas_segitiga = luas_persegi / 2

# menghitung luas lingkaran
luas_lingkaran = (math.pi * ((panjang_persegi / 2) ** 2)) / 2

# menghitung luas trapesium
luas_trapesium = ((panjang_persegi + panjang_trapesium) * panjang_persegi) / 2

# perhitungan akhir
# menghitung luas 1 nametag
luas_nametag = luas_persegi + luas_segitiga + luas_lingkaran + luas_trapesium

# menghitung luas total nametag sesuai yang di input user
total_luas_nametag = luas_nametag * banyak_nametag

# menghitung uang yang diperlukan untuk membeli kertas dengan harga Rp0.40/cm^2
uang_diperlukan = total_luas_nametag * 0.4
# membulatkan uang yang diperlukan menjadi ribuan atas terdekat
pembulatan_uang_diperlukan = math.ceil(uang_diperlukan / 1000) * 1000


# menampilkan hasil dan ringkasan
print(f"\nHalo, {nama}! Berikut informasi terkait nametag kamu:\n")
print(f"Luas 1 nametag: {round(luas_nametag, 2)} cm^2")
print(f"Luas total nametag: {round(total_luas_nametag, 2)} cm^2")
print(f"Uang yang diperlukan: Rp{pembulatan_uang_diperlukan}")
