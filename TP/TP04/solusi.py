import random
from tkinter import *
import tkinter.ttk as ttk

class Menu:
    def __init__(self, kode_menu, nama_menu, harga):
        self.kode_menu = kode_menu
        self.nama_menu = nama_menu
        self.harga = int(harga)

    def get_kode(self):
        return self.kode_menu

    def get_nama(self):
        return self.nama_menu

    def get_harga(self):
        return self.harga
    
    def get_info_tambahan(self):
        pass


class Meals(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        self.tingkat_kegurihan = int(tingkat_kegurihan)


class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        self.tingkat_kemanisan = int(tingkat_kemanisan)


class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        self.tingkat_keviralan = int(tingkat_keviralan)

    
class Table:
    nama_orang = ''
    isTaken = False
    meals = []

    def __init__(self, nomor_meja):
        self.nomor_meja = nomor_meja

    def get_nama_orang(self):
        return self.nama_orang
    
    def get_nomor_meja(self):
        return self.nomor_meja
    
    def get_isTaken(self):
        return self.isTaken
    
    def get_meals(self):
        return self.meals
    
    def set_nama_orang(self, nama_orang):
        self.nama_orang = nama_orang
    
    def set_isTaken(self, isTaken):
        self.isTaken = isTaken
    
    def set_meals(self, meals):
        self.meals = meals

    def find_total_price(self):
        total_price = 0
        for meal in self.meals:
            total_price += meal[2]*meal[4]
        return total_price

    def __str__(self):
        return "Meja dengan nomor " + str(self.get_nomor_meja())

    def __repr__(self):
        return str(self)

def createMenu(kode_menu, nama_menu, harga, jenis, info_tambahan):
    if jenis == 'MEALS':
        return Meals(kode_menu, nama_menu, harga, info_tambahan)
    elif jenis == 'DRINKS':
        return Drinks(kode_menu, nama_menu, harga, info_tambahan)
    else:
        return Sides(kode_menu, nama_menu, harga, info_tambahan)
    
def findTable(table_list, nomor_meja):
    for table in table_list:
        if table.get_nomor_meja() == nomor_meja:
            return 


class Display(object):
    def __init__(self):
        self.window = Tk()
        self.window.title("Kafe Daun-Daun Pacilkom v2.0")
        self.window.geometry("400x200")
        self.window.resizable(False, False)

        self.frame1 = Frame(self.window)
        self.frame2 = Frame(self.window)
        self.frame3 = Frame(self.window)
        self.frame_table = Frame(self.window)
        self.frame4 = Frame(self.window)
        
        self.set_menu()
        self.landing_page()

        self.window.mainloop()

    def set_menu(self):
        with open('menu.txt', 'r') as f:
            lines = f.read().splitlines() 

        # filled with menu tuple, form tuplenya (kode, nama_menu, harga, extra_info) --> Sesuai sama di soal
        self.menu_list_tuple = []
        self.menu_jenis = {}
        self.menu_kode = {}

        # filled with table OBJECTS
        self.table_list = []

        self.vacant_table = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.used_table = []

        # constructing meal, drink, side object an putting it into menu list from menu.txt
        jenis = ""
        for element in lines:
            if (element.startswith("===")):
                jenis = element.strip().replace("===", "")
            else:
                element_attributes = element.split(';')
                menu = createMenu(element_attributes[0], element_attributes[1], element_attributes[2], jenis, element_attributes[3])
                menu_tuple = (menu.get_kode(), menu.get_nama(), menu.get_harga(), menu.get_info_tambahan())
                self.menu_list_tuple.append(menu_tuple)

                if jenis not in self.menu_jenis.keys():
                    self.menu_jenis[jenis] = []
                self.menu_jenis[jenis].append(menu_tuple)
                self.menu_kode[menu.get_kode()] = menu
            
        for nomor_meja in range(9):
            self.table_list.append(Table(nomor_meja+1))


    def landing_page(self):
        self.frame2.forget()
        self.frame1.pack()

        button1 = Button(self.frame1, text="Buat Pesanan", width=20, command=self.buat_pesanan)
        button2 = Button(self.frame1, text="Selesai Gunakan Meja", width=20)
        button1.grid(row=0, column=0, padx=10, pady=40)
        button2.grid(row=1, column=0)

    def buat_pesanan(self):
        self.frame1.forget()
        self.frame2.pack()

        label = Label(self.frame2, text="Siapa nama Anda?")
        entry = Entry(self.frame2)
        button1 = Button(self.frame2, text="Kembali", width=20, command=self.landing_page)
        button2 = Button(self.frame2, text="Lanjut", width=20, command=lambda: self.daftar_menu(entry.get()))

        label.grid(column=0, row=0, pady=(80,0))
        entry.grid(column=1, row=0, pady=(80,0))
        button1.grid(column=0, row=1, padx=(0,5), pady=(60,0))
        button2.grid(column=1, row=1, padx=(5,0), pady=(60,0))

    def daftar_menu(self, nama):
        self.frame2.forget()
        self.frame3.pack()
        self.frame_table.pack()
        self.frame4.pack()

        self.window.geometry("600x600")

        random_table = random.choice(self.vacant_table)

        label_nama = Label(self.frame3, text="Nama pemesan: " + str(nama))
        label_meja = Label(self.frame3, text="No Meja: " + str(random_table))
        button_ubah = Button(self.frame3, text="Ubah")
      
        label_nama.grid(column=0, row=0, padx=(0,100), pady=(0,20))
        label_meja.grid(column=2, row=0, pady=(0,20))
        button_ubah.grid(column=3, row=0, pady=(0,20))

        self.comboboxes = {}
        cols = len(self.menu_list_tuple[0])
        curr_row = 0
        for jenis in self.menu_jenis.keys():
            curr_row += 1
            label_jenis = Label(self.frame_table, text=jenis)
            label_jenis.grid(column=0, row=curr_row)
            for menu_tuple in self.menu_jenis[jenis]:
                curr_row += 1
                for j in range(cols-1):
                    entry = Entry(self.frame_table, width=20)
                    entry.grid(row=curr_row, column=j)
                    entry.insert(END, menu_tuple[j])
                    entry['state'] = 'readonly'
                
                values = tuple([k for k in range(10)])
                opsi_jumlah = ttk.Combobox(self.frame_table, values=values, state='readonly')
                opsi_jumlah.current(0)
                opsi_jumlah.bind('<<ComboboxSelected>>', lambda event, kode_menu=menu_tuple[0]: self.hitung_total(event, kode_menu))
                self.comboboxes[menu_tuple[0]] = opsi_jumlah
                opsi_jumlah.grid(row=curr_row, column=cols-1)

        self.total_harga = 0
        self.label_harga = Label(self.frame4, text="Total harga: 0")
        self.label_harga.grid(column=3, row=0)

        self.current_pesanan = {}
    
    def hitung_total(self, event, kode_menu):
        combobox = self.comboboxes[kode_menu]
        self.current_pesanan[kode_menu] = int(combobox.get())

        harga = 0
        for kode in self.current_pesanan.keys():
            menu = self.menu_kode[kode]
            harga += self.current_pesanan[kode] * menu.get_harga()

        self.label_harga.config(text="Total harga: " + str(harga))

def main():
    Display()
    
if __name__ == "__main__":
    main()

