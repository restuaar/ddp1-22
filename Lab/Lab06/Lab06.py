# Restu Ahmad Ar Ridho
# NPM : 2206028951
# Lab 06

# melakukan import libabry yang dibutuhkan
from math import floor

print("Selamat mencoba Program Pemeriksa Nilai Dek Depe!")
print("=================================================\n")

# deklarasi list untuk menampung kunci jawaban dan jawaban kamu
lst_kunci = []
lst_jawaban = []

# meminta input untuk kunci jawaban
kunci_jawaban = input("Masukkan kunci jawaban:\n")
while kunci_jawaban != "STOP":
    lst_kunci.append(kunci_jawaban) # memasukan kedalam list agar dapat disimpan
    kunci_jawaban = input()

# deklarasi banyak soal
BANYAK_SOAL = len(lst_kunci)

# meminta input untuk jawaban kamu sesuai dengan banyak soal
print("Masukkan kunci jawaban kamu:")
for i in range(BANYAK_SOAL):
    jawaban_kamu = input()
    lst_jawaban.append(jawaban_kamu) # memasukan kedalam list agar dapat disimpan

# mengecek setiap elemen dan menyimpan dalam list True or False
lst_jawaban_benar = [lst_kunci[x] == lst_jawaban[x] for x in range(BANYAK_SOAL)]

# deklarasi jumlah soal yang benar
BANYAK_SOAL_BENAR = lst_jawaban_benar.count(True)

print()

# menghitung nilai dari banyak soal
nilai = floor((BANYAK_SOAL_BENAR/BANYAK_SOAL) * 100)
# membagi kasus untuk setiap nilai
if nilai >= 85:
    print("Selamat :D")
elif 55 <= nilai < 85:
    print("Semangat :)")
else:
    print("nt")

print(f"Total jawaban benar adalah {BANYAK_SOAL_BENAR} dari {BANYAK_SOAL} soal")
print(f"Nilai yang kamu peroleh adalah {nilai}")