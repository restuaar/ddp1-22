# Restu Ahmad Ar Ridho
# NPM : 2206028951

print("Selamat Datang di Bunker Hacker!\n")

# Meminta input dari user
banyak_konversian = int(input("Masukkan berapa kali konversi yang ingin dilakukan: "))
print()

# Melakukan looping untuk berapa banyak konversian yang dilakukan sesuai dengan input
for i in range(1,banyak_konversian+1):
    # Meminta angka desimal dari user
    desimal = int(input(f"Masukkan angka ke-{i} yang ingin dikonversikan (dalam desimal): "))
    # Deklarasi string kosong untuk menyimpan sisa pembagian sementara
    temp_sisa_hasil_pembagian = ""
    # Melakukan looping hingga desimal menjadi 0
    while desimal != 0:
        # Melakukan penyimpanan sisa pembagian
        temp_sisa_hasil_pembagian += str(desimal%8)
        # Melakukan floor division untuk modulo selanjutnya
        desimal = desimal//8
    # Melakukan reverse string
    octal = temp_sisa_hasil_pembagian[::-1]
    # Menampilkan hasil
    print(f"Hasil konversi desimal ke basis 8 : {octal}")
    print()

print("Terima kasih telah menggunakan Bunker Hacker!")