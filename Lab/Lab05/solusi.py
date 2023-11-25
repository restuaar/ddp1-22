import math

def kerucut():
    r = float(input("Masukkan jari-jari kerucut : "))
    t = float(input("Masukkan tinggi kerucut : "))
    volume = 1/3 * math.pi * (r**2) * t
    return volume

def balok():
    p = float(input("Masukkan panjang balok : "))
    l = float(input("Masukkan lebar balok : "))
    t = float(input("Masukkan tinggi balok : "))
    volume = p * l * t
    return volume

print("Selamat datang di Depot Minuman Dek Depe")
print("==========================================")
param = True
total_volume = 0
while param:
    validator = input("Masukkan bentuk galon yang diinginkan (STOP untuk berhenti): ")
    
    if (validator == "KERUCUT"):
        total_volume += kerucut()
    elif (validator == "BALOK"):
        total_volume += balok()
    elif (validator == "STOP"):
        param = False
    else :
        print("Input tidak benar, masukkan kembali")
    print()

if (total_volume == 0):
    print("====================================================")
    print("Anda tidak memasukkan input satupun :(")
    print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")
    print("====================================================")

else :
    print("====================================================")
    print(f"Total volume air yang dikeluarkan adalah : {total_volume:.2f}")
    print(f"Total harga yang harus dibayar adalah : Rp{((total_volume * 700)):.2f}")
    print("====================================================")
    print("Terima kasih telah menggunakan Depot Air Minum Dek Depe")