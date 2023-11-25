print("Selamat Datang di Bunker Hacker!")
print()

n = int(input("Masukkan berapa kali konversi yang ingin dilakukan: "))
print()

for i in range(n):
    x = int(input("Masukkan angka ke-" + str(i + 1) + " yang ingin dikonversikan (dalam desimal): "))
    
    # Inisialisasi string kosong result untuk mengumpulkan sisa pembagian x dengan 8
    result = ""

    # Lakukan pembagian dan simpan modulo sampai temporary > 0 
    while x > 0:
        # Menambahkan sisa pembagian x dengan 8 ke result
        result += str(x % 8)
        
        # Floor division x dengan 8 hingga x habis
        x //= 8

    # Setelah result didapatkan, reverse string result
    result = result[::-1]
    
    # print result akhir
    print("Hasil konversi desimal ke basis 8 :", result)
    print()

print("Terima kasih telah menggunakan Bunker Hacker!")