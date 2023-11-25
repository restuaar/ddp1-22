# import modul 
from tkinter import Label, Button, Entry, Tk, StringVar, Frame
from tkinter.messagebox import showinfo
import tkinter as tk
import tkinter.ttk as ttk
import random

class Main:
    def __init__(self, master):
        
        # mengatur judul dan background
        self.master = master
        self.frm = Frame(master)
        self.master.geometry('375x150')
        

        self.frm.grid()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        
        # membuat tulisan dan tombol
        self.label = Label(self.frm, text= "Selamat datang di Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.label.grid(row=0, column = 1, padx = 50, pady = 10)

        self.button = Button(self.frm, text = "BUAT PESANAN", command = self.buat_pesanan)
        self.button.grid(row=1, column=1, pady = 5)

        self.button = Button(self.frm, text = "SELESAI GUNAKAN MEJA", command = self.selesai)
        self.button.grid(row=2, column=1, pady = 5)
        
    def buat_pesanan(self):
        buat_pesanan_window = Tk()
        form1 = BuatPesanan(buat_pesanan_window)
        buat_pesanan_window.mainloop()

    def selesai(self):
        selesai_window = Tk()
        form2 = Selesai(selesai_window)
        selesai_window.mainloop()


class BuatPesanan:

    def __init__ (self, master):
        
        # mengatur judul dan background
        self.master = master
        self.master.geometry('375x150')

        master.title('Kafe Daun-Daun Pacilkom v2.0 🌿')
        self.frm = Frame(master)
        self.frm.grid(padx=35, pady=10)

        self.label = Label(self.frm, text = 'Form Buat Pesanan')
        self.label.grid(row=0, column = 1)

        self.frame1 = Frame(self.frm,height=100)
        self.frame1.grid(row=1, column = 1, pady=20)

        self.label = Label(self.frame1, text='Siapa Nama Anda?')
        self.nama_pemesan = StringVar()
        self.field_nama_pemesan = Entry(self.frame1, textvariable = self.nama_pemesan, width = 30)
        self.label.grid(row=1, column=0), self.field_nama_pemesan.grid(row=1, column=1, padx = 10)
        
        self.frame2 = Frame(self.frm,height=100)
        self.frame2.grid(row=2, column = 1)

        self.button = Button(self.frame2, text = "Kembali")
        self.button.grid(row=2, column=0, pady = 10, padx=10)

        self.button = Button(self.frame2, text = "Lanjut", command = self.show_nama)
        self.button.grid(row=2, column=1, pady = 10)

        self.total = Label(self.master,text = "Total Pesanan: 0")
        self.nomor_meja = Label(self.master,text = "Nomor Meja: -")


    def show_nama(self):

        if self.field_nama_pemesan.get() == '':
            showinfo(message=f'Harap lengkapi nama pemesan')
        else :
            nama_pemesan = self.field_nama_pemesan.get()  
            self.frm.destroy()
            self.master.geometry('525x500')
            meja_random = random.choice(cafe_kami.get_meja_kosong())
            new_pesanan = Pesanan(nama_pemesan, meja_random)

            create_halaman_pesanan(self, new_pesanan)

    def simpann(self, pesanan):
        showinfo(message=f'Pesanan Tersimpan')
        dct_pesanan_meja[pesanan.get_meja()] = pesanan
        print(dct_pesanan_meja)
        cafe_kami.get_meja_kosong().remove(pesanan.get_meja())
        cafe_kami.get_meja_terisi().append(pesanan.get_meja())
        self.master.destroy()


def create_halaman_pesanan(master, pesanan):
    header = Frame(master.master)
    header.grid(row=0, column=0, pady=10)

    label = Label(header, text = f'Nama Pemesan: {pesanan.get_pemesan()}' )
    label.grid(row=0, column = 0)

    meja_ubah = Frame(header)
    master.nomor_meja = Label(meja_ubah,text = f"Nomor Meja: {pesanan.get_meja()}")
    master.nomor_meja.grid(row=0, column = 0)

    kosong = Frame(header, width=250)
    kosong.grid(row=0, column=1)

    def ubah_meja():
        ubah_meja = Tk()
        form2 = UbahMeja(ubah_meja, pesanan, master)
        ubah_meja.mainloop()

    button = Button(meja_ubah, text = "Ubah", command=ubah_meja)
    button.grid(row=0, column=1)
    meja_ubah.grid(row=0, column = 3)


    body = Frame(master.master)
    body.grid(row=1, column=0, padx=20)

    table_a = Frame(body)

    label = Label(table_a, text = 'Meals')
    label.grid(row=0, column = 0)
    table = Table(cafe_kami.get_kumpulan_meals(), "meals", pesanan, master,table_a)
    table.grid(row=1, column = 0)
    kosong = Frame(table, height=10)
    kosong.grid(row=2, column=1)


    label = Label(table_a, text = 'Drinks')
    label.grid(row=3, column = 0)
    table = Table(cafe_kami.get_kumpulan_drinks(), "drinks", pesanan, master,table_a)
    table.grid(row=4, column = 0)
    kosong = Frame(table, height=10)
    kosong.grid(row=5, column=1)

    label = Label(table_a, text = 'Sides')
    label.grid(row=6, column = 0)
    table = Table(cafe_kami.get_kumpulan_sides(), "sides", pesanan, master,table_a)
    table.grid(row=7, column = 0)
    kosong = Frame(table, height=10)
    kosong.grid(row=8, column=1)

    table_a.grid()

    master.total.grid()


    tempat_tombol = Frame(master.master)
    button = Button(tempat_tombol, text = "Kembali")
    button.grid(row=0, column=0, pady = 10, padx=10)

    button = Button(tempat_tombol, text = "Simpan",command=lambda: master.simpann(pesanan))
    button.grid(row=0, column=1, pady = 10)
    tempat_tombol.grid(row=9, column=0)



class UbahMeja:

    def __init__ (self, master, pesanan, frame_sblmnya):
        
        # mengatur judul dan background
        self.master = master
        self.pesanan = pesanan
        self.frame_sblmnya = frame_sblmnya

        self.label = Label(self.master, text = 'Silakan pilih meja kosong yang diinginkan')
        self.label.grid(row=0, column = 0, pady=10)

        self.frm = Frame(master)
        self.frm.grid(row=1, column=0)

        self.master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.master.geometry('300x450')

        self.temp_meja = pesanan.get_meja()

        def create_button(text, bg, command):
            if bg == None:
                return Button(self.frm, text = f"{text}", width=17, command=lambda: self.set_temp_meja(command))
            return Button(self.frm, text = f"{text}", width=17, bg=bg, command=lambda: self.set_temp_meja(command))


        for i in range (10): 
            if i == pesanan.get_meja():
                self.button = create_button(i, "blue", i)

            elif i in cafe_kami.get_meja_kosong():
                self.button = create_button(i, None, i)
                
            else : 
                self.button = create_button(i, "red", i)

            if i%2:
                self.button.grid(row=i//2, column=1, padx=10, pady=10)
            else:
                self.button.grid(row=i//2, column=0, padx=10, pady=10)

    
        self.label = Label(self.master, text = 'Info')
        self.label.grid(row=2, column = 0)
        self.label = Label(self.master, text = 'Merah: Terisi')
        self.label.grid(row=3, column = 0)
        self.label = Label(self.master, text = 'Abu-abu: Kosong')
        self.label.grid(row=4, column = 0)
        self.label = Label(self.master, text = 'Biru: Meja Anda')
        self.label.grid(row=5, column = 0)

        self.tempat_tombol = Frame(self.master)
        self.button = Button(self.tempat_tombol, text = "Kembali")
        self.button.grid(row=0, column=0, pady = 10, padx=10)

        self.button = Button(self.tempat_tombol, text = "Simpan", command=self.simpan)
        self.button.grid(row=0, column=1, pady = 10)
        self.tempat_tombol.grid(row=6, column=0)


    def set_temp_meja(self, nomor):
        self.temp_meja = nomor


    def simpan(self):
        self.pesanan.set_meja(self.temp_meja)
        self.master.destroy()
        self.frame_sblmnya.nomor_meja.config(text = "Nomor Meja: " + str(self.pesanan.get_meja()))


class Table(tk.Frame):
  def __init__(self, data, tipe, pesanan,sblm, master, jml=None):
    super().__init__(master)
    self.grid()
    self.data = data
    self.total_rows = len(self.data)
    self.total_columns = 5
    self.tipe = tipe
    self.pesanan = pesanan
    self.frame_sblmnya = sblm
    self.jml = jml
    self.generate_table()
 
  def generate_table(self):
    entry = tk.Entry(self, width = 10)
    entry.grid(row = 0, column = 0)
    entry.insert(tk.END, "Kode")
    entry['state'] = 'readonly'

    entry = tk.Entry(self, width = 20)
    entry.grid(row = 0, column = 1)
    entry.insert(tk.END, "Nama")
    entry['state'] = 'readonly'

    entry = tk.Entry(self, width = 20)
    entry.grid(row = 0, column = 2)
    entry.insert(tk.END, "Harga")
    entry['state'] = 'readonly'

    entry = tk.Entry(self, width = 10)
    entry.grid(row = 0, column = 3)
    if self.tipe == "meals":
        entry.insert(tk.END, "Kegurihan")
    elif self.tipe =="drinks":
        entry.insert(tk.END, "Kemanisan")
    else :
        entry.insert(tk.END, "Keviralan")
    entry['state'] = 'readonly'

    entry = tk.Entry(self, width = 15)
    entry.grid(row = 0, column = 4)
    entry.insert(tk.END, "Jumlah")
    entry['state'] = 'readonly'

    def create_row(i):
        entry = tk.Entry(self, width = 10)
        entry.grid(row = i, column = 0)
        entry.insert(tk.END, self.data[i-1].get_kode())
        entry['state'] = 'readonly'

        entry = tk.Entry(self, width = 20)
        entry.grid(row = i, column = 1)
        entry.insert(tk.END, self.data[i-1].get_nama())
        entry['state'] = 'readonly'

        entry = tk.Entry(self, width = 20)
        entry.grid(row = i, column = 2)
        entry.insert(tk.END, self.data[i-1].get_harga())
        entry['state'] = 'readonly'

        entry = tk.Entry(self, width = 10)
        entry.grid(row = i, column = 3)
        if self.tipe == "meals":
            entry.insert(tk.END, self.data[i-1].get_gurih())
        elif self.tipe =="drinks":
            entry.insert(tk.END, self.data[i-1].get_manis())
        else :
            entry.insert(tk.END, self.data[i-1].get_viral())
        entry['state'] = 'readonly'
        
        if self.jml == None:
            values = tuple([k for k in range(10)])

            selected = StringVar()
            opsi_jumlah = ttk.Combobox(self, values = values, width=10, textvariable=selected)

            def jumlah_changed(event):
                """ handle the month changed event """

                self.pesanan.get_list_pesanan()[self.data[i-1]] = opsi_jumlah.get()
                print(self.pesanan.get_list_pesanan())
                self.frame_sblmnya.total.config(text = "Total Pesanan: " + self.pesanan.get_total())

            opsi_jumlah.bind('<<ComboboxSelected>>', jumlah_changed)
            opsi_jumlah.grid(row = i, column = self.total_columns - 1)
        
        else:
            entry = tk.Entry(self, width = 15)
            entry.grid(row = i, column = 4)
            entry.insert(tk.END, self.jml[i-1])
            entry['state'] = 'readonly'

    for i in range(1, self.total_rows+1):
        create_row(i)
        
class Selesai:

    def __init__ (self, master):        
        self.master = master
        self.frm = Frame(master)
        self.frm.grid()

        self.label = Label(self.master, text = 'Silakan klik meja yang selesai digunakan')
        self.label.grid(row=0, column = 0, pady=10)

        self.frm = Frame(master)
        self.frm.grid(row=1, column=0)

        self.master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.master.geometry('300x450')
        self.kursi_terisi()

    def kursi_terisi(self):

        def create_button(text, bg, command):
            if bg == None:
                return Button(self.frm, text = f"{text}", width=17)
            return Button(self.frm, text = f"{text}", width=17, bg=bg, command=lambda: self.tampilkan(command))


        for i in range (10): 
            if i in cafe_kami.get_meja_kosong():
                self.button = create_button(i, None, None)
                
            else : 
                self.button = create_button(i, "red", dct_pesanan_meja[i])

            if i%2:
                self.button.grid(row=i//2, column=1, padx=10, pady=10)
            else:
                self.button.grid(row=i//2, column=0, padx=10, pady=10)

    
        self.frm2 = Frame(self.master)
        self.frm2.grid(row=2, column=0)
        self.label = Label(self.frm2, text = 'Info')
        self.label.grid(row=2, column = 0)
        self.label = Label(self.frm2, text = 'Merah: Terisi')
        self.label.grid(row=3, column = 0)
        self.label = Label(self.frm2, text = 'Abu-abu: Kosong')
        self.label.grid(row=4, column = 0)

        self.tempat_tombol = Frame(self.frm2)
        self.button = Button(self.tempat_tombol, text = "Kembali")
        self.button.grid(row=0, column=0, pady = 10, padx=10)

        self.button = Button(self.tempat_tombol, text = "Simpan")
        self.button.grid(row=0, column=1, pady = 10)
        self.tempat_tombol.grid(row=6, column=0)

    def tampilkan(self, pesanan) :
        self.frm2.destroy()
        self.frm.destroy()

        self.master.geometry('525x500')

        self.frm = Frame(self.master)
        self.frm.grid(row=1, column=0)
        header = Frame(self.frm)
        header.grid(row=0, column=0, pady=10)

        label = Label(header, text = f'Nama Pemesan: {pesanan.get_pemesan()}' )
        label.grid(row=0, column = 0)

        meja_ubah = Frame(header)
        self.master.nomor_meja = Label(meja_ubah,text = f"Nomor Meja: {pesanan.get_meja()}")
        self.master.nomor_meja.grid(row=0, column = 0)

        kosong = Frame(header, width=250)
        kosong.grid(row=0, column=1)

        meja_ubah.grid(row=0, column = 3)


        body = Frame(self.frm)
        body.grid(row=1, column=0, padx=20)

        table_a = Frame(body)
        list_jumlah_meals = [0 for i in range (len(cafe_kami.get_kumpulan_meals()))]
        list_jumlah_drinks = [0 for i in range (len(cafe_kami.get_kumpulan_drinks()))]
        list_jumlah_sides = [0 for i in range (len(cafe_kami.get_kumpulan_sides()))]
        list_pesanan = pesanan.get_list_pesanan()

        for i in list_pesanan.keys():
            if i.get_tipe() == "Meals":
                list_jumlah_meals[cafe_kami.get_kumpulan_meals().index(i)] = list_pesanan[i]
            elif i.get_tipe() == "Drinks":
                list_jumlah_drinks[cafe_kami.get_kumpulan_drinks().index(i)] = list_pesanan[i]
            elif i.get_tipe() == "Sides":
                list_jumlah_sides[cafe_kami.get_kumpulan_sides().index(i)] = list_pesanan[i]
        print(list_jumlah_drinks)
        print(list_jumlah_meals)
        print(list_jumlah_sides)

        label = Label(table_a, text = 'Meals')
        label.grid(row=0, column = 0)
        table = Table(cafe_kami.get_kumpulan_meals(), "meals", pesanan, self.master, table_a, list_jumlah_meals)
        table.grid(row=1, column = 0)
        kosong = Frame(table, height=10)
        kosong.grid(row=2, column=1)


        label = Label(table_a, text = 'Drinks')
        label.grid(row=3, column = 0)
        table = Table(cafe_kami.get_kumpulan_drinks(), "drinks", pesanan, self.master, table_a, list_jumlah_drinks)
        table.grid(row=4, column = 0)
        kosong = Frame(table, height=10)
        kosong.grid(row=5, column=1)

        label = Label(table_a, text = 'Sides')
        label.grid(row=6, column = 0)
        table = Table(cafe_kami.get_kumpulan_sides(), "sides", pesanan, self.master, table_a,list_jumlah_sides)
        table.grid(row=7, column = 0)
        kosong = Frame(table, height=10)
        kosong.grid(row=8, column=1)

        table_a.grid()

        label = Label(self.master, text = f'Total: {pesanan.get_total()}')
        label.grid(row=9, column = 0)

        self.frm2 = Frame(self.master)
        self.frm2.grid(row=2, column=0)

        self.tempat_tombol = Frame(self.frm2)
        self.button = Button(self.tempat_tombol, text = "Kembali")
        self.button.grid(row=0, column=0, pady = 10, padx=10)

        self.button = Button(self.tempat_tombol, text = "Hapus", command=lambda: self.hapus(pesanan))
        self.button.grid(row=0, column=1, pady = 10)
        self.tempat_tombol.grid(row=6, column=0)

    def hapus(self, pesanan):
        dct_pesanan_meja.pop(pesanan.get_meja())
        print(cafe_kami.get_meja_kosong())
        print(cafe_kami.get_meja_terisi())
        cafe_kami.get_meja_kosong().append(pesanan.get_meja())
        cafe_kami.get_meja_terisi().remove(pesanan.get_meja())
        self.master.destroy()        


class Pesanan() : 
    def __init__(self, pemesan, meja, lst_pesanan = {}):
        self.__pemesan = pemesan
        self.__meja = meja
        self.__list_pesanan = lst_pesanan

    def get_pemesan(self):
        return self.__pemesan

    def get_meja(self):
        return self.__meja

    def set_meja(self, meja):
        self.__meja = meja

    def get_list_pesanan(self):
        return self.__list_pesanan

    def get_total(self):
        total = 0
        for i in self.__list_pesanan.keys():
            total += i.get_harga() *  int(self.__list_pesanan[i])

        return str(total)

class Cafe():
    def __init__(self, kumpulan_meals = [], kumpulan_drinks = [], kumpulan_sides = [], meja_kosong = [i for i in range(10)], meja_terisi = []):
        self.__kumpulan_meals = kumpulan_meals
        self.__kumpulan_drinks = kumpulan_drinks
        self.__kumpulan_sides = kumpulan_sides
        self.__meja_kosong = meja_kosong
        self.__meja_terisi = meja_terisi

    def get_kumpulan_meals(self):
        return self.__kumpulan_meals

    def get_kumpulan_drinks(self):
        return self.__kumpulan_drinks

    def get_kumpulan_sides(self):
        return self.__kumpulan_sides

    def get_meja_kosong(self):
        return self.__meja_kosong

    def get_meja_terisi(self):
        return self.__meja_terisi
    
class Menu() : 
    
    # constructor yang meng-assign kode, nama, harga
    def __init__(self, kode, nama, harga):
        self.__kode = kode
        self.__nama = nama
        self.__harga = int(harga)

    def get_kode(self): 
        return self.__kode

    def get_nama(self): 
        return self.__nama
    
    def get_harga(self): 
        return self.__harga

    def __str__(self): 
        return f"Nama: {self.__nama}\nKode: {self.__kode}\nHarga: {self.__harga}\nTipe: {self.get_tipe()}\n"

class Meals(Menu):

    # constructor yang meng-assign kode, nama, harga
    def __init__(self, kode, nama, harga, gurih):
        super().__init__(kode, nama, harga)

        # atribut khusus kelas fiksi adalah genre
        self.__gurih = int(gurih)

    def get_gurih(self): 
        return self.__gurih

    def get_tipe(self): 
        return "Meals"


class Drinks(Menu):
    
    # constructor yang meng-assign kode, nama, harga
    def __init__(self, kode, nama, harga, manis):
        super().__init__(kode, nama, harga)

        # atribut khusus kelas fiksi adalah genre
        self.__manis = int(manis)

    def get_manis(self): 
        return self.__manis

    def get_tipe(self): 
        return "Drinks"

class Sides(Menu):

    # constructor yang meng-assign kode, nama, harga
    def __init__(self, kode, nama, harga, viral):
        super().__init__(kode, nama, harga)

        # atribut khusus kelas fiksi adalah genre
        self.__viral = int(viral)

    def get_viral(self): 
        return self.__viral

    def get_tipe(self): 
        return "Sides"

cafe_kami = Cafe()
dct_pesanan_meja = {}

# Memulai program
def main():
    file = open("menu.txt", "r")
    menus = file.read().split("===")

    for menu in menus:
        if menu:
            lst_per_jenis = menu.split("\n")
            jenis = lst_per_jenis[0]

            for i in range(1, len(lst_per_jenis)):
                food = lst_per_jenis[i]

                if food:
                    food_detail = food.split(";")

                    kode = food_detail[0]
                    nama = food_detail[1]
                    harga = food_detail[2]
                    extra = food_detail[3]

                    if jenis == "MEALS" : 
                        menu_obj = Meals(kode, nama, harga, extra)
                        cafe_kami.get_kumpulan_meals().append(menu_obj)

                    elif jenis == "DRINKS":
                        menu_obj = Drinks(kode, nama, harga, extra)
                        cafe_kami.get_kumpulan_drinks().append(menu_obj)

                    elif jenis == "SIDES":
                        menu_obj = Sides(kode, nama, harga, extra)
                        cafe_kami.get_kumpulan_sides().append(menu_obj)

    window = Tk()
    cafe = Main(window)
    window.mainloop() 

if __name__ == '__main__':
    main()
