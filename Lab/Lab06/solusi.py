# waktu pengerjaan +- 9 menit

print(
    """
Selamat mencoba Program Pemeriksa Nilai Dek Depe!
=================================================
"""
)

kunjaw = []
print("Masukkan kunci jawaban: ")
while True:
    command = input()
    if command != "STOP":
        kunjaw.append(command)
    else:
        break

jawaban_benar = []
print("Masukkan jawaban kamu:")
for i in range(len(kunjaw)):
    ans = input()
    if ans == kunjaw[i]:
        jawaban_benar.append(ans)


nilai = 100 * len(jawaban_benar) // len(kunjaw)

if nilai >= 85:
    print("Selamat :D")
elif 55 <= nilai < 85:
    print("Semangat :)")
else:
    print("nt")

print(f"Total jawaban benar adalah {len(jawaban_benar)} dari {len(kunjaw)} soal")
print("Nilai yang kamu peroleh adalah", nilai)