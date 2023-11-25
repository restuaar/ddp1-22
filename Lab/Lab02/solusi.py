# Solusi DDP2 2022/2023 Lab 2
print("Selamat datang ke Dek Depe Holiday Tracker!")
print()
banyak_tempat_wisata = int(
    input("Masukkan banyak tempat wisata yang kamu kunjungi: "))

# Pengecekan validitas input
while banyak_tempat_wisata <= 0:
    print()
    print("Input tidak valid. Silahkan masukkan input kembali!")
    banyak_tempat_wisata = int(
        input("Masukkan banyak tempat wisata kamu yang kamu kunjungi: "))

# Penjumlahan tingkat kebahagiaan Dek Depe
tingkat_kebahagiaan = 0
rating_tertinggi = 0
tamasya_paling_berkesan_terakhir = ""

for i in range(banyak_tempat_wisata):
    print()
    tujuan_wisata = input(f"Perjalanan {i+1}: ")
    rating = int(input(f"Rating perjalanan kamu ke {tujuan_wisata} (indeks 1-10): "))

    tingkat_kebahagiaan += rating

    if rating >= rating_tertinggi:
        tamasya_paling_berkesan_terakhir = tujuan_wisata
        rating_tertinggi = rating

# Tips: Pembagian pada Python akan menghasilkan float walaupun operand berupa int
rata_rata_kebahagiaan = tingkat_kebahagiaan / banyak_tempat_wisata

print()
print("---Summary---")
print(f"Perjalanan paling mengesankan adalah ketika pergi ke {
      tamasya_paling_berkesan_terakhir}.")
print(f"Skala kebahagiaan Dek Depe adalah {rata_rata_kebahagiaan:.2f}")

# Pengecekan overall experience Dek Depe
if 8 <= rata_rata_kebahagiaan <= 10:
    print("Dek Depe bahagia karena pengalamannya menyenangkan.")
elif 5 <= rata_rata_kebahagiaan < 8:
    print("Dek Depe senang karena pengalamannya cukup baik.")
else:
    print("Dek Depe sedih karena pengalamannya buruk.")

print()
print("Terimakasih telah menggunakan Dek Depe Holiday Tracker!")
