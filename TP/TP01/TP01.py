# Restu Ahmad Ar Ridho
# NPM : 2206028951

# Import library yang diperlukan
import turtle as t
from tkinter.messagebox import showerror
from random import randint

# Menyeting judul, background color, kecepatan menggambar, membuat warna rgb menjadi range 0-255, dan menghilangkan ikon turtle
t.title("TP1")
t.bgcolor("green")
t.speed("fastest")
t.colormode(255)
t.hideturtle()

# Meminta input lapisan bawah
while True:
    lapisan_bawah = t.numinput("Input Lapisan Bawah","Jumlah batu bata pada lapisan paling bawah:",minval=1,maxval=25)
    if lapisan_bawah != int(lapisan_bawah): # Mengecek apakah input bilangan bulat atau tidak
        showerror("Error","Input lapisan bawah tidak boleh koma. Coba lagi!")
    else:
        break
lapisan_bawah = int(lapisan_bawah)

# Meminta input lapisan atas
while True:
    lapisan_atas = t.numinput("Input Lapisan Atas","Jumlah batu bata pada lapisan paling atas:",minval=1,maxval=lapisan_bawah)
    if lapisan_atas != int(lapisan_atas): # Mengecek apakah input bilangan bulat atau tidak
        showerror("Error","Input lapisan atas tidak boleh koma. Coba lagi!")
    else:
        break
lapisan_atas = int(lapisan_atas)

# Meminta input panjang bata
while True:
    panjang_bata = t.numinput("Input Panjang Bata","Panjang satu buah batu bata (piksel):",minval=1,maxval=35)
    if panjang_bata != int(panjang_bata): # Mengecek apakah input bilangan bulat atau tidak
        showerror("Error","Input panjang bata tidak boleh koma. Coba lagi!")
    else:
        break
panjang_bata = int(panjang_bata)

# Meminta input lebar bata
while True:
    lebar_bata = t.numinput("Input Lebar Bata","Lebar satu buah batu bata (piksel):",minval=1,maxval=25)
    if lebar_bata != int(lebar_bata): # Mengecek apakah input bilangan bulat atau tidak
        showerror("Error","Input lebar bata tidak boleh koma. Coba lagi!")
    else:
        break
lebar_bata = int(lebar_bata)

# Deklarasi variabel untuk menentukan posisi lapisan bata di tengah
temp_posisi_x = -int((panjang_bata * lapisan_bawah)/2)
temp_posisi_y = -int(((lebar_bata * (lapisan_bawah - lapisan_atas + 1))/2))

# Deklarasi variabel untuk lapisan berikutnya
temp_lapisan_bawah = lapisan_bawah

# Deklrasi variabel panjang dan lebar bata sementara agar dapat mengatur posisi lapisan bata yang diatasnya
temp_panjang_bata = panjang_bata
temp_lebar_bata = lebar_bata

# Deklarasi variabel menyimpan jumlah bata
jumlah_bata = 0

while lapisan_atas != (temp_lapisan_bawah+1): # Membuat looping untuk mencetak setiap lapisan bata
    # Menuju koordinat untuk mencetak lapisan bata
    t.penup()
    t.goto((temp_posisi_x+int(temp_panjang_bata/2)-20),temp_posisi_y+temp_lebar_bata)
    t.pendown()
    
    # Membuat looping agar 1 bata menjadi lapisan bata
    for i in range(temp_lapisan_bawah):
    # Membagi kasus menjadi 2 warna bata
        if (lapisan_bawah == temp_lapisan_bawah) or (i == 0) or (i == (temp_lapisan_bawah-1)) or (lapisan_atas == temp_lapisan_bawah):
            # Jika bata merupakan lapisan bawah, lapisan atas, bata paling kiri atau kanan setiap lapisan maka akan memiliki warna #bc4a3c
            t.fillcolor("#BC4A3C")
        else:
            # Jika bata merupakan bagian tengah maka bata warna warni menggunakan rgb
            t.fillcolor(randint(0,255),randint(0,255),randint(0,255))
        t.begin_fill() # Memulai mode mengisi warna bata
        # Membuat looping untuk mencetak 1 bata
        for j in range(2):
            t.forward(panjang_bata)
            t.left(90)
            t.forward(lebar_bata)
            t.left(90)
        t.end_fill() # Mengakhiri mode mengisi warna bata
        t.forward(panjang_bata) # Untuk menuju penggambaran bata disampingnya
        jumlah_bata += 1 # Menghitung jumlah bata

    # Penambahan untuk menentukan posisi lapisan berikutnya dan mengurangi jumlah bata pada lapisan berikutnya
    temp_panjang_bata += panjang_bata
    temp_lebar_bata += lebar_bata
    temp_lapisan_bawah -= 1

# Mencetak teks yang menampilkan jumlah bata yang digunakan
t.penup()
# Membuat kasus sesuai dengan output candi
t.goto(-290,temp_posisi_y-25)
if (jumlah_bata == 1) or (lapisan_atas == lapisan_bawah):
    t.write(f"1 lapisan batu bata dengan jumlah {jumlah_bata} batu bata",False,align="left",font=("Arial", 20, "normal"))    
elif (lapisan_bawah == (lapisan_atas+1)):
    t.write(f"2 lapisan batu bata dengan jumlah {jumlah_bata} batu bata",False,align="left",font=("Arial", 20, "normal"))    
elif jumlah_bata == 6:
    t.goto(-160,temp_posisi_y-25)
    t.write(f"Candi dengan 6 batu bata",False,align="left",font=("Arial", 20, "normal"))
else:
    t.goto(-255,temp_posisi_y-25)
    t.write(f"Candi warna-warni dengan {jumlah_bata} batu bata",False,align="left",font=("Arial", 20, "normal"))

t.exitonclick()