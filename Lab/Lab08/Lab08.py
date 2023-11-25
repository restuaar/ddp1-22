# Restu Ahmad Ar Ridho
# NPM : 2206028951
# Lab 07

def jarak_kenal(person1,person2,total):
    global data_hub, data_jarak
    """
    Fungsi untuk menghitung jarak
    """
    # Base Case
    if person1 == person2: # Ketika orang yang dicari sudah sama dengan hubungannya
        return total
    elif not(person1 in data_hub): # Ketika person2 tidak terdapat hubungan
        return -1
    
    # Recursive Case
    else:
        person = data_hub[person1] # Mengubah param person1 menjadi hubungannya
        return jarak_kenal(person,person2,(total + data_jarak[person1]))

# Deklarasi dictionary untuk antara hubungan dan jarak
data_hub = {}
data_jarak = {}

print("Masukkan data hubungan: ")

# Meminta input dan memasukan data kedalam dictionary
temp = input()
while temp != "SELESAI":
    lst_temp = temp.split()
    data_hub[lst_temp[0]] = lst_temp[1]
    data_jarak[lst_temp[0]] = float(lst_temp[2])
    temp = input()
print()

# Meminta input yang dicari
person1 = input("Masukkan nama awal: ")
person2 = input("Masukkan nama tujuan: ")

# Menghitung jarak dengan fungsi recursive
total_jarak = jarak_kenal(person1,person2,0) * 10

# Jika total jarak dengan jarak koma 0
if total_jarak == int(total_jarak):
    total_jarak = int(total_jarak)

# Membagi kasus berdasarkan total jarak
if total_jarak == -10:
    print(f"Tidak ada hubungan antara {person1} dan {person2}.")
elif total_jarak > 1000:
    print(f"Jarak total: {total_jarak}")
    print(f"{person1} dan {person2} tidak saling kenal.")
elif 100 < total_jarak <= 1000:
    print(f"Jarak total: {total_jarak}")
    print(f"{person1} dan {person2} mungkin saling kenal.")
elif 0 < total_jarak <= 100:
    print(f"Jarak total: {total_jarak}")
    print(f"{person1} dan {person2} kenalan dekat.")