# Restu Ahmad Ar Ridho
# NPM : 2202068951

print("Selamat datang ke Dek Depe Holiday Tracker!\n")

# Meminta input dari user untuk banyak tempat wisata yang dikunjungi
banyak_tempat_wisata = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
print()

# Membuat program jika input kurang sama dengan 0 maka menampilkan tidak valid dan mengulangi pertanyaan
while banyak_tempat_wisata<=0:
    print("Input tidak valid. Silahkan masukkan input kembali!")
    banyak_tempat_wisata = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
    print()

# Deklarasi variabel untuk menyimpan tempat terfavorit dan juga skala favorit agar bisa dibandingkan dengan skala perjalanan lainnya
temp_tempat_perjalanan = ""
temp_rating_perjalanan = 0

# Deklarasi variabel untuk menyimpan total rating perjalanan
total_kebahagiaan = 0

# Melakakukan looping untuk tempat dan rating perjalanan sesuai dengan banyak tempat wisata yang diinput
for i in range(1,banyak_tempat_wisata+1):
    # Meminta input dari user untuk Nama perjalanan dan juga skalanya
    tempat_perjalanan = input(f"Perjalanan {i}: ")
    rating_perjalanan = int(input(f"Rating perjalanan kamu ke Balairung (indeks 1-10): "))
    print()
    # Membandingkan rating yang baru diinput dengan rating yang sudah disimpan dalam variable temp
    if rating_perjalanan>=temp_rating_perjalanan:
        temp_rating_perjalanan = rating_perjalanan # Menyimpan variable yang besar
        temp_tempat_perjalanan = tempat_perjalanan # Menyimpan nama tempat sesuai dengan rating
    # Melakukan pertambahan untuk total rating
    total_kebahagiaan += rating_perjalanan 

# Membagi total rating dengan banyaknya perjalanan agar menjadi skala kebahagiaan
skala_kebahagiaan = (total_kebahagiaan/banyak_tempat_wisata)

# Menampilkan hasil
print("--Summary--")
print(f"Perjalanan paling mengesankan adalah ketika pergi ke {temp_tempat_perjalanan}.")
print(f"Skala kebahagiaan Dek Depe adalah {round(skala_kebahagiaan, 2)}")

# Membuat program agar skala kebahagiaan sesuai dengan overall pengalaman Dek Depe
if 8<=skala_kebahagiaan<=10:
    print("Dek Depe bahagia karena pengalamannya menyenangkan.")
elif 5<=skala_kebahagiaan<8:
    print("Dek Depe senang karena pengalamannya cukup baik.")
elif skala_kebahagiaan<5:
    print("Dek Depe sedih karena pengalamannya buruk.")
print("\nTerimakasih telah menggunakan Dek Depe Holiday Tracker!")