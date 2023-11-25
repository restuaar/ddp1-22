# Restu Ahmad Ar Ridho
# NPM : 2206028951
# Lab 05

# Men-import libary yang dibutuhkan
from math import pi

# Deklarasi konstanta
PI = pi
HARGA = 700

# Membuat fungsi untuk menghitung volume balok
def volume_balok(panjang:float,lebar:float,tinggi:float) -> float:
    """
    fungsi untuk menghitung volume sebuah balok
    """
    return panjang*lebar*tinggi

# Membuat fungsi untuk menghitung volume kerucut
def volume_kerucut(jari:float,tinggi:float) -> float:
    """
    fungsi untuk menghitung volume sebuah kerucut
    """
    return (1/3)*PI*(jari**2)*tinggi


print("Selamat datang di Depot Minuman Dek Depe!")
print("="*41)

# Deklarasi variable untuk menampung total volume dan membuat variabel untuk lanjut atau tidak
isLanjut = True
total_volume = 0

# Membuat looping untuk menanyakan terus apakah ingin pengisian galon lanjut atau tidak
while isLanjut:
    # Membuat looping untuk jika yang diinput tidak sesuai dengan yang diinginkan
    while True:
        bentuk_galon = input("Masukkan bentuk galon yang diinginkan (STOP) untuk berhenti: ")

        # Membagi kasus ketika isiin bentuk galon STOP
        if bentuk_galon == "STOP":
            isLanjut = False
            break

        # Membagi kasus ketika isiin bentuk galon sesuai dengan keinginan
        elif (bentuk_galon == "BALOK") or (bentuk_galon == "KERUCUT"):

            # Jika bentuk balok maka akan dihitung sebagai volume balok
            if bentuk_galon == "BALOK":
                panjang = float(input(f"Masukkan panjang {bentuk_galon.lower()}: "))
                lebar = float(input(f"Masukkan lebar {bentuk_galon.lower()}: "))
                tinggi = float(input(f"Masukkan tinggi {bentuk_galon.lower()}: "))
                temp_volume = volume_balok(panjang,lebar,tinggi)

            # Jika bentuk kerucut maka akan dihitung sebagai volume kerucut
            elif bentuk_galon == "KERUCUT":
                jari = float(input(f"Masukkan jari-jari {bentuk_galon.lower()}: "))
                tinggi = float(input(f"Masukkan tinggi {bentuk_galon.lower()}: "))
                temp_volume = volume_kerucut(jari,tinggi)
    
            total_volume += temp_volume
            print()

        # Membagi kasus ketika isiin bentuk galon tidak sesuai keinginan
        else:
            print("Input tidak benar, masukkan kembali\n")

# Menghitung total harga
total_harga = total_volume * HARGA
print()

# Membagi kasus untuk output apakah volume dikeluarkan atau tidak sama sekali
if total_volume == 0:
    print("="*53)
    print(f"Anda tidak memasukkan input satupun :(")
    print("="*53)
else:
    print("="*53)
    print(f"Total volume air yang dikeluarkan adalah: {total_volume: .2f}")
    print(f"Total harga yang harus dibayarkan adalah: Rp{total_harga: .2f}")
    print("="*53)

print("\nTerima kasih telah menggunakan Depot Air Minum Dek Depe")