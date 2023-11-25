# Restu Ahmad Ar Ridho
# NPM : 2206028951
# TP 4

# Import modul yang diperlukan
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.messagebox import showinfo
from random import randint

# Membuat objek Menu untuk menyimpan data menu
class Menu:
    # Constractor
    def __init__(self, kode_menu, nama_menu, harga):
        self.__kode_menu = kode_menu
        self.__nama_menu = nama_menu
        self.__harga = int(harga)

    # Menambahkan fungsi getter
    def get_kode_menu(self):
        return self.__kode_menu
    def get_nama_menu(self):
        return self.__nama_menu
    def get_harga(self):
        return self.__harga

    # Sebagai representasi jika objek dipanggil
    def __repr__(self) -> str:
        return self.__nama_menu

# Membuat objek Meals yang merupakan sub class dari Menu
class Meals(Menu):
    # Constractor
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kegurihan):
        super().__init__(kode_menu, nama_menu, harga)
        self.__tingkat_kegurihan = tingkat_kegurihan

    # Fungsi getter
    def get_tingkat_kegurihan(self):
        return self.__tingkat_kegurihan
    def get_all_attribute(self):
        return [self.get_kode_menu(),self.get_nama_menu(),self.get_harga(),self.get_tingkat_kegurihan()]

# Membuat objek Drinks yang merupakan sub class dari Menu
class Drinks(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_kemanisan):
        super().__init__(kode_menu, nama_menu, harga)
        self.__tingkat_kemanisan = tingkat_kemanisan

    # Fungsi getter
    def get_tingkat_kemanisan(self):
        return self.__tingkat_kemanisan
    def get_all_attribute(self):
        return [self.get_kode_menu(),self.get_nama_menu(),self.get_harga(),self.get_tingkat_kemanisan()]

# Membuat objek Sides yang merupakan sub class dari Menu
class Sides(Menu):
    def __init__(self, kode_menu, nama_menu, harga, tingkat_keviralan):
        super().__init__(kode_menu, nama_menu, harga)
        self.__tingkat_keviralan = tingkat_keviralan

    # Fungsi getter
    def get_tingkat_keviralan(self):
        return self.__tingkat_keviralan
    def get_all_attribute(self):
        return [self.get_kode_menu(),self.get_nama_menu(),self.get_harga(),self.get_tingkat_keviralan()]

# Membuat objek Meja sebagai tempat penyimpan data pada setiap meja
class Meja():
    # Constractor
    def __init__(self,no_meja):
        self.__no_meja = no_meja
        self.__nama_cus = None
        self.__pesanan = None
        self.__kosong = True
        self.__total_harga = 0
    
    # Fungsi getter
    def get_no_meja(self):
        return self.__no_meja
    def get_nama_cus(self):
        return self.__nama_cus
    def get_pesanan(self):
        return self.__pesanan
    def get_kosong(self):
        return self.__kosong
    def get_total_harga(self):
        return self.__total_harga

    # Fungsi setter
    def set_nama_cus(self,param):
        self.__nama_cus = param
    def set_pesanan(self,param):
        self.__pesanan = param
    def set_kosong(self,param):
        self.__kosong = param
    def set_total_harga(self,param):
        self.__total_harga = param

    # Sebagai representasi ketika objek dipanggil
    def __repr__(self) -> str:
        return str(self.__no_meja)

# Membuat objek sebagai frame untuk main window (master) gui
class Main(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        # Menyetel tampilan window GUI
        self.master.geometry("400x200")
        self.pack()
        self.master.resizable(False,False)
        self.master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")

        # Button untuk melanjutkan ke Input Nama Customer atau Selesai Menggunakan Meja
        self.button1 = tk.Button(self, text="Buat Pesanan", width=30, 
                            command=self.buat_pesanan, bg="#4472C4", fg="white")
        self.button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30,  
                            command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        self.button1.grid(row=0, column=0, padx=10, pady=40)
        self.button2.grid(row=1, column=0)

    def buat_pesanan(self):
        BuatPesanan(self.master)

    def selesai_gunakan_meja(self):
        SelesaiGunakanMeja(self.master)

# Membuat objek window baru ketika user melanjutkan ke Input Nama Customer
class BuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        # Menyetel tampilan window GUI
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.resizable(False,False)

        # Widget label dan tempat input user untuk Nama Customer
        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.lbl_nama.grid(column=0, row=0, pady=(80,0), padx=(45,5))
        self.customer = tk.StringVar()
        self.field_name = tk.Entry(self, textvariable=self.customer)
        self.field_name.grid(column=1, row=0, pady=(80,0), padx=(5,45))

        # Button untuk kembali ke Main Window atau Melanjutkan Pesanan
        self.button1 = tk.Button(self, text="Kembali", width=20, command=self.destroy, bg="#4472C4", fg="white")
        self.button2 = tk.Button(self, text="Lanjut", width=20, command=self.buat_pesanan_lanjut, 
                                bg="#4472C4", fg="white")
        self.button1.grid(column=0, row=1, pady=(60,15), padx=(45,5))
        self.button2.grid(column=1, row=1, pady=(60,15), padx=(5,45))

    # Fungsi untuk Melanjutkan Pesanan
    def buat_pesanan_lanjut(self):
        global meja, temp_no_meja

        self.meja_penuh = False
        self.temp_count_meja = 0
        # Mencari meja yang kosong
        for no_meja in range(len(meja)):
            # Jika ada yang kosong maka proses pemesanan berlanjut
            if meja[no_meja].get_kosong() == True:
                meja_benar = True
                while meja_benar:
                    # Random tempat duduk
                    no_meja_new = randint(0,9)
                    if meja[no_meja_new].get_kosong() == True:
                        # Membagi kasus ketika customer tidak menginput nama
                        if self.customer.get() == "":
                            meja[no_meja_new].set_nama_cus("Customer")
                        else:
                            meja[no_meja_new].set_nama_cus(self.customer.get())
                        meja[no_meja_new].set_kosong(False) # Melakukan set untuk meja sedang dipakai
                        temp_no_meja = no_meja_new # Menyimpan ke variabel global untuk meja yang sedang di urus
                        meja_benar = False
                break
            self.temp_count_meja += 1
        self.temp_count_meja += 1
        # Handle untuk seluruh meja penuh
        if self.temp_count_meja == 11:
            self.meja_penuh = True

        self.destroy()
        if self.meja_penuh: # Ketika meja penuh maka pesanan tidak dilanjutkan
            showinfo(title="Kafe Daun-Daun Pacilkom v2.0 🌿", 
                        message="“Mohon maaf, meja sedang penuh. Silakan datang kembali di lain kesempatan.")
        else: # Melanjutkan pesanan
            PesananLanjutan(self.master)

# Membuat objek window baru jika user melanjutkan pesanan
class PesananLanjutan(tk.Toplevel):
    def __init__(self, master):
        global meja, temp_cus, temp_no_meja
        super().__init__(master)
        # Menyetel tampilan window GUI
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.resizable(False,False)

        # Mengambil data dari objek meja
        self.meja_customer = meja[temp_no_meja]

        # Membuat table untuk pesanan
        Table(menus,self).grid(column=0,columnspan=4,row=0, padx=(10,10))
        # Tombol untuk Kembali dan Ok yang berarti menyimpan pesanan
        self.button1 = tk.Button(self, text="Kembali", width=20, command=self.kembali, bg="#4472C4", fg="white")
        self.button2 = tk.Button(self, text="OK", width=20, command=self.menyimpan_pesanan, bg="#4472C4", fg="white")
        self.button1.grid(column=1, row=1, pady=(60,15), padx=(45,5), sticky="e")
        self.button2.grid(column=2, row=1, pady=(60,15), padx=(5,45), sticky="w")

    # Fungsi untuk User menekan tombol OK
    def menyimpan_pesanan(self):
        global pesanan, total_harga, temp_nama_cus, temp_no_meja, menus
        # Handle jika user tidak menginput makanan berarti asumsi memesan makanan yang berjumlah 0
        if pesanan == None:
            self.count = 0
            for item in menus:
                for menu in menus[item]:
                    self.count += 1
            pesanan = [x - x for x in range(self.count)] # Membuat jumlah makanan 0
            total_harga = 0
        # Mennyimpan ke dalam objek Meja sesuai dengan no mejanya
        self.meja_customer.set_pesanan(pesanan)
        self.meja_customer.set_total_harga(total_harga)

        # Mengembalikan variabel global kembali ke awal
        pesanan = total_harga = temp_no_meja = temp_nama_cus = None
        self.destroy()
    
    # Fungsi untuk User menekan tombol Kembali
    def kembali(self):
        global temp_no_meja, meja
        # Mengembalikan attribute objek meja kembali ke awal
        meja[temp_no_meja].set_nama_cus(None)
        meja[temp_no_meja].set_kosong(True)
        temp_no_meja = None

        self.destroy()
        BuatPesanan(self.master) # Kembali ke Customer input nama

# Membuat class Table sebagai widget untuk PesananLanjutan
class Table(tk.Frame):
    def __init__(self, data, master = None):
        super().__init__(master)
        global temp_no_meja, meja
        # Mengambil data dari objek meja
        self.meja_customer = meja[temp_no_meja]
        self.total_harga = self.meja_customer.get_total_harga()

        # Inisiasi variabel awal
        self.list_jumlah = [] # Untuk jumlah setiap menu yang dipesan (combobox)
        self.list_harga = [] # Harga pada setiap menu yang dipesan
        self.data = data # Menu
        # Variabel untuk membuat tabel
        self.total_columns = 5
        self.row = 1
        self.current_index = 0
        
        # Label untuk nama pemesan dan no meja yang sedang digunakan serta tombol untuk mengubah meja
        self.customer = tk.Label(self, text=f"Nama pemesan: {self.meja_customer.get_nama_cus()}")
        self.customer.place(x=0, y=0)
        self.no_meja = tk.Label(self, text=f"No Meja: {self.meja_customer.get_no_meja()}")
        self.no_meja.grid(column=3,row=0,sticky="e")
        self.no_meja_button = tk.Button(self, text="Ubah", command=self.ubah_meja,bg="#4472C4", fg="white")
        self.no_meja_button.grid(column=4,row=0,sticky="w")

        self.generate_table() # Membuat tabel

        # Label harga
        self.label_harga = tk.Label(self, text=f"Total harga: Rp 0", font="Helvatica 11 bold")
        self.label_harga.grid(column=3, columnspan=2, row=self.row+1, padx=(92,0))

    # Fungsi untuk membuat table helper
    def generate_table_helper(self,item,header):
        self.label_menu = tk.Label(self, text=item).grid(column=0,row=self.row) # Group menu
        self.row += 1
        for h in range(self.total_columns): # Sebagai header pada setiap group menu
            self.entry = tk.Entry(self, width = 20)
            self.entry.grid(row = self.row, column = h)
            self.entry.insert(tk.END, header[h])
            self.entry['state'] = 'readonly'
        self.row += 1
        # Membuat dan memasukan data kedalam table
        for menu in self.data[item]:
            self.temp_menu = menu.get_all_attribute() # Mengambil data untuk setiap Menu
            for j in range(self.total_columns):
                if j == 4: # Jika kolom paling terakhir yang berisi combobox
                    values = tuple([k for k in range(10)])
                    self.list_jumlah.append(tk.IntVar()) # Menyimpan tempat untuk tempat combobox dalam list
                    self.list_harga.append(self.temp_menu[2]) # Menyimpan harga
                    # Membuat combobox dan bind untuk setiap kali value combobox berubah
                    self.combobox = ttk.Combobox(self, values = values, 
                                                textvariable=self.list_jumlah[self.current_index])
                    self.combobox.grid(row = self.row, column = self.total_columns - 1)
                    self.combobox.bind("<<ComboboxSelected>>", self.update_total)
                    self.combobox.bind("<<KeyRelease>>", self.update_total)
                    continue
                # Membuat tabel berupa data Menu
                self.entry = tk.Entry(self, width = 20)
                self.entry.grid(row = self.row, column = j)
                self.entry.insert(tk.END, self.temp_menu[j])
                self.entry['state'] = 'readonly'
            self.row += 1
            self.current_index += 1

    # Fungsi untuk membuat table yand dibedakan setiap headernya
    def generate_table(self):
        for item in self.data:
            if item == "MEALS":
                self.header = ["Kode", "Nama", "Harga", "Kegurihan", "Jumlah"]
                self.generate_table_helper(item,self.header)
            elif item == "DRINKS":
                self.header = ["Kode", "Nama", "Harga", "Kemanisan", "Jumlah"]
                self.generate_table_helper(item,self.header)
            elif item == "SIDES":
                self.header = ["Kode", "Nama", "Harga", "Keviralan", "Jumlah"]
                self.generate_table_helper(item,self.header)

    # Fungsi ketika setiap kali value combobox berubah
    def update_total(self,event):
        global pesanan, total_harga
        self.temp = 0
        self.temp_pesanan = []
        # Menyimpan banyak yang dipesan kedalam variabel global pesanan dan total harga agar disimpan sementara
        for i in range(len(self.list_jumlah)):
            self.temp_pesanan.append(self.list_jumlah[i].get())
            self.harga = self.list_jumlah[i].get() * self.list_harga[i]
            self.temp += self.harga
        pesanan = self.temp_pesanan
        total_harga = self.temp
        # Agar dapat live update
        self.label_harga["text"] = f"Total harga: Rp {self.temp}"

    # Fungsi ketika Customer menekan tombol ubah meja
    def ubah_meja(self):
        global meja, temp_no_meja,temp_nama_cus,temp_ubah_meja
        # Mengambil data sebelum meja dipindah dan disimpan dalam variabel global
        temp_ubah_meja = meja[temp_no_meja].get_no_meja()
        temp_nama_cus = meja[temp_no_meja].get_nama_cus()
        # Menyetel attribute meja sebelumnya menjadi kembali ke awal
        meja[temp_no_meja].set_nama_cus(None)
        meja[temp_no_meja].set_kosong(True)
        self.master.destroy()
        UbahMeja(self.master.master) # Menuju window Ubah Meja

# Objek untuk window ketika user meminta Ubah Meja
class UbahMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        global meja, temp_cus
        # Menyetel tampilan window GUI
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.resizable(False,False)

        # Label tulisan
        self.label_atas = tk.Label(self, text="Silakan klik meja kosong yang diinginkan:")
        self.label_atas.grid(column=0, columnspan=2, row=0,pady=(0,20))

        # Membuat tombol meja
        TableMeja(self).grid(column=0, columnspan=2, row=1)

        # Label info
        self.label_info = tk.Label(self, text="Info", font="Helvatica 11 bold")
        self.label_info_merah = tk.Label(self, text="Merah: Terisi")
        self.label_info_abu = tk.Label(self, text="Abu-abu: Kosong")
        self.label_info_biru = tk.Label(self, text="Biru: Meja Anda")
        self.label_info.grid(column=0, row=2, sticky="w", padx=30)
        self.label_info_merah.grid(column=0, row=3, sticky="w", padx=30)
        self.label_info_abu.grid(column=0, row=4, sticky="w", padx=30)
        self.label_info_biru.grid(column=0, row=5, sticky="w", padx=30)

        # Tombol untuk kembali dan menyimpan hasil ubah meja
        self.button1 = tk.Button(self, text="Kembali", width=20, command=self.kembali, bg="#4472C4", fg="white")
        self.button2 = tk.Button(self, text="OK", width=20, command=self.update_meja, bg="#4472C4", fg="white")
        self.button1.grid(column=0, row=6, pady=(20,40), padx=(50,5))
        self.button2.grid(column=1, row=6, pady=(20,40), padx=(5,50))
    
    # Fungsi ketika customer memindahkan mejanya
    def update_meja(self):
        global temp_nama_cus,temp_no_meja,meja,menus
        # Menyetel kembali attribute objek sesuai dengan meja yang dituju
        meja[temp_no_meja].set_nama_cus(temp_nama_cus)
        meja[temp_no_meja].set_kosong(False)

        self.destroy()
        PesananLanjutan(self.master.master) # Kembali ke window Pesanan

    # Fungsi ketika customer tidak jadi mengubah mejanya
    def kembali(self):
        global temp_no_meja,temp_ubah_meja,meja,menus
        # Menyetel ulang ke objek meja sebelumnya yang sudah setel ke awal
        meja[temp_ubah_meja].set_nama_cus(temp_nama_cus)
        meja[temp_ubah_meja].set_kosong(False)
        temp_no_meja = temp_ubah_meja # Menyimpan meja customer yang sedang memesan

        self.destroy()
        PesananLanjutan(self.master.master) # Kembali ke window Pesanan Lanjutan

# Membuat class Tombol Meja sebagai widget untuk Ubah Meja
class TableMeja(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        global temp_no_meja, meja
        # Variabel untuk membuat tombol meja
        self.row = 0
        self.column = 0
        # Variabel untuk menyimpan setiap button agar dapat di ubah warnanya ketika update meja
        self.button = []

        self.generate() # Membuat tombol

    # Fungsi untuk membuat tombol meja
    def generate(self):
        for no_meja in range(len(meja)):
            # Bagi kasus ketika attribute objek meja kosong, meja sendiri, dan tidak kosong
            if temp_no_meja == meja[no_meja].get_no_meja():
                self.bg_color = "#4472C4"
                self.state = tk.DISABLED
            elif not meja[no_meja].get_kosong():
                self.bg_color = "Red"
                self.state = tk.DISABLED
            else:
                self.bg_color = "#b0aa99"
                self.state = tk.NORMAL

            # Membuat tombol meja
            if self.row == 5:
                self.row = 0
                self.column += 1
                # Membuat tombol sesuai dengan attribute pada setiap meja dan fungsi sesuai dengan no meja
                self.button_meja = tk.Button(self, text=meja[no_meja].get_no_meja(), width=10, height=1, 
                                            command=lambda no = no_meja: self.ubah_no_meja(no), 
                                            bg=self.bg_color, fg="white", state=self.state)
                self.button_meja.grid(column=self.column, row=self.row, padx=5,pady=5)
                self.row += 1
                self.button.append(self.button_meja)
                continue
            # Membuat tombol sesuai dengan attribute pada setiap meja dan fungsi sesuai dengan no meja
            self.button_meja = tk.Button(self, text=meja[no_meja].get_no_meja(), width=10, height=1, 
                                            command=lambda no = no_meja: self.ubah_no_meja(no), 
                                            bg=self.bg_color, fg="white",state=self.state)
            self.button_meja.grid(column=self.column, row=self.row, padx=5, pady=5)
            self.row += 1
            # Memasukan setiap tombol kedalam suatu variabel list agar dapat diubah
            self.button.append(self.button_meja)

    # Ketika user menekan tombol pada tombol yang dipilih
    def ubah_no_meja(self,no_meja):
        global temp_no_meja
        # Menyetel agar tampilan tombol meja sebelumnya menjadi biasa
        self.button_cur = self.button[temp_no_meja]
        self.button_cur["bg"] = "#b0aa99"
        self.button_cur["state"] = tk.NORMAL

        # Menyetel tampilan tombol meja yang dipilih
        temp_no_meja = no_meja
        self.button_cur = self.button[temp_no_meja]
        self.button_cur["bg"] = "#4472C4"
        self.button_cur["state"] = tk.DISABLED

# Membuat objek window baru ketika user melanjutkan ke Selesai Menggunakan Meja dari main window
class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        global temp_no_meja, meja
        super().__init__(master)
        # Menyetel tampilan window GUI
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.resizable(False,False)

        # Label tulisan 
        self.label_atas = tk.Label(self, text="Silakan klik meja yang selesai digunakan:")
        self.label_atas.grid(column=0, columnspan=2, row=0,pady=(0,5), padx=60)

        # Membuat tombol meja
        TableMejaSelesai(self).grid(column=0, columnspan=2, row=1, padx=60)

        # Label info
        self.label_info = tk.Label(self, text="Info", font="Helvatica 11 bold")
        self.label_info_merah = tk.Label(self, text="Merah: Terisi")
        self.label_info_abu = tk.Label(self, text="Abu-abu: Kosong")
        self.label_info.grid(column=0, row=2, sticky="w", padx=30)
        self.label_info_merah.grid(column=0, row=3, sticky="w", padx=30)
        self.label_info_abu.grid(column=0, row=4, sticky="w", padx=30)

        # Button untuk kembali ke main window
        self.button1 = tk.Button(self, text="Kembali", width=20, command=self.destroy, bg="#4472C4", fg="white")
        self.button1.grid(column=0,columnspan=2, row=6, pady=(20,40), padx= 60)

# Membuat class Tombol Meja sebagai widget untuk Selesai Menggunakan Meja
class TableMejaSelesai(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        global temp_no_meja, meja
        # Variabel untuk membuat tombol meja
        self.row = 0
        self.column = 0

        self.generate() # Membuat tombol

    # Fungsi untuk membuat setiap tombol no meja
    def generate(self):
        for no_meja in range(len(meja)):
            # Bagi kasus ketika attribute objek meja kosong dan tidak kosong
            if not meja[no_meja].get_kosong():
                self.bg_color = "Red"
                self.state = tk.NORMAL
            else:
                self.bg_color = "#b0aa99"
                self.state = tk.DISABLED
            # Membuat tombol meja
            if self.row == 5:
                self.row = 0
                self.column += 1
                # Membuat tombol sesuai dengan attribute pada setiap meja dan fungsi sesuai dengan no meja
                self.button_meja = tk.Button(self, text=meja[no_meja].get_no_meja(), width=10, height=1, 
                                            command=lambda no = no_meja: self.selesai_no_meja(no), 
                                            bg=self.bg_color, fg="white", state=self.state)
                self.button_meja.grid(column=self.column, row=self.row, padx=5,pady=5)
                self.row += 1
                continue
            # Membuat tombol sesuai dengan attribute pada setiap meja dan fungsi sesuai dengan no meja
            self.button_meja = tk.Button(self, text=meja[no_meja].get_no_meja(), width=10, height=1, 
                                            command=lambda no = no_meja: self.selesai_no_meja(no), 
                                            bg=self.bg_color, fg="white",state=self.state)
            self.button_meja.grid(column=self.column, row=self.row, padx=5, pady=5)
            self.row += 1

    # Fungsi ketika customer menekan tombol meja yang ingin diselesaikan
    def selesai_no_meja(self,no_meja):
        global temp_no_meja, menus
        # Menyimpan no meja kedalam variabel global agar dapat digunakan kembali
        temp_no_meja = no_meja
        self.master.destroy()
        CheckOut(self.master.master) # Menuju window yang berisi pesanan pada meja tersebut

# Objek untuk window ketika user Ingin Menyelesaikan Meja yang menampilkan pesanannya
class CheckOut(tk.Toplevel):
    def __init__(self, master):
        global meja, temp_cus, temp_no_meja
        super().__init__(master)
        # Menyetel tampilan window GUI
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.resizable(False,False)

        # Mengambil data dari objek meja
        self.meja_customer = meja[temp_no_meja]

        # Membuat tabel yang berisi pesanan pada meja tersebut
        TableCheckout(menus,self).grid(column=0,columnspan=4,row=0, padx=(10,10))

        # Tombol untuk Kembali ke pilih meja dan Selesai Menggunakan Meja
        self.button1 = tk.Button(self, text="Kembali", width=20, command=self.kembali, bg="#4472C4", fg="white")
        self.button2 = tk.Button(self, text="Selesai Gunakan Meja", width=20, command=self.selesai_gunakan_meja, 
                                bg="#4472C4", fg="white")
        self.button1.grid(column=1, row=1, pady=(60,15), padx=(45,5), sticky="e")
        self.button2.grid(column=2, row=1, pady=(60,15), padx=(5,45), sticky="w")
    
    # Ketika customer menekan tombol kembali
    def kembali(self):
        self.destroy()
        SelesaiGunakanMeja(self.master) # Menuju window pilih meja

    # Ketika customer menekan tombol Sselesai Menggunakan Meja
    def selesai_gunakan_meja(self):
        global pesanan, total_harga, temp_nama_cus, temp_no_meja
        # Menyetel kembali setiap attribute objek meja yang dipilih ke awal
        self.meja_customer.set_nama_cus(None)
        self.meja_customer.set_pesanan(None)
        self.meja_customer.set_kosong(True)
        self.meja_customer.set_total_harga(0)
        # Menyetel variabel global ke awal
        pesanan = total_harga = temp_no_meja = temp_nama_cus = None
        self.destroy()
        SelesaiGunakanMeja(self.master) # Menuju window pilih meja

# Membuat class table yang berisi pesanan meja sebagai widget untuk window CheckOut
class TableCheckout(tk.Frame):
    def __init__(self, data, master = None):
        global meja,temp_no_meja
        super().__init__(master)
        # Mengambil data dari objek meja yang dipilih
        self.meja_customer = meja[temp_no_meja]
        self.pesanan = self.meja_customer.get_pesanan()
        self.data = data # Menu

        # Variabel untuk membuat tabel pesanan pada meja
        self.total_columns = 5
        self.row = 1
        self.current_index = 0

        # Label nama pemesan dan no meja
        self.customer = tk.Label(self, text=f"Nama pemesan: {self.meja_customer.get_nama_cus()}")
        self.customer.place(x=0,y=0)
        self.no_meja = tk.Label(self, text=f"No Meja: {self.meja_customer.get_no_meja()}")
        self.no_meja.grid(column=3,row=0,sticky="e")

        self.generate_table() # Membuat tabel

        # Label untuk total harga
        self.label_harga = tk.Label(self, text=f"Total harga: Rp {self.meja_customer.get_total_harga()}", 
                                    font="Helvatica 11 bold")
        self.label_harga.grid(column=3,columnspan=2,row=self.row+1, padx=(72,0))

    # Fungsi untuk membuat tabel pesanan
    def generate_table_helper(self,item,header):
        self.label_menu = tk.Label(self, text=item).grid(column=0,row=self.row) # Label group menu
        self.row += 1
        for h in range(5): # Sebagai header pada setiap group menu
            self.entry = tk.Entry(self, width = 20)
            self.entry.grid(row = self.row, column = h)
            self.entry.insert(tk.END, header[h])
            self.entry['state'] = 'readonly'
        self.row += 1
        # Membuat dan memasukan data kedalam tabel
        for menu in self.data[item]:
            # Mengambil setiap attribute pada setiap jenis menu
            self.temp_menu = menu.get_all_attribute()
            for j in range(5):
                if j == 4: # Jika kolum paling kanan menurupakan pesanan customer
                    self.entry = ttk.Entry(self, width=20)
                    self.entry.grid(row = self.row, column = 4)
                    self.entry.insert(tk.END, self.pesanan[self.current_index])
                    self.entry['state'] = 'readonly'
                    continue
                # Membuat tabel berupa data menu
                self.entry = tk.Entry(self, width = 20)
                self.entry.grid(row = self.row, column = j)
                self.entry.insert(tk.END, self.temp_menu[j])
                self.entry['state'] = 'readonly'
            self.row += 1
            self.current_index += 1

    # Fungsi untuk membuat table yand dibedakan setiap headernya
    def generate_table(self):
        for item in self.data:
            if item == "MEALS":
                self.header = ["Kode", "Nama", "Harga", "Kegurihan", "Jumlah"]
                self.generate_table_helper(item,self.header)
            elif item == "DRINKS":
                self.header = ["Kode", "Nama", "Harga", "Kemanisan", "Jumlah"]
                self.generate_table_helper(item,self.header)
            elif item == "SIDES":
                self.header = ["Kode", "Nama", "Harga", "Keviralan", "Jumlah"]
                self.generate_table_helper(item,self.header)

# Fungsi utama
def main():
    global menus
    # Membaca dan menyimpan menu sesuai format
    with open('menu.txt', 'r') as f:
        lines = f.read().splitlines() 
        current_menu = ""
        # Menyimpan group menu
        for item in lines:
            if item.startswith("==="):
                current_menu = item[3:]
                menus[current_menu] = []
            else:
                split_line = item.split(";")
                kode,nama,harga,tingkat = split_line
                # Menyimpan setiap jenis menu sesuai dengan objek menunya
                if current_menu == "MEALS":
                    menus[current_menu].append(Meals(kode,nama,harga,tingkat))
                elif current_menu == "DRINKS":
                    menus[current_menu].append(Drinks(kode,nama,harga,tingkat))
                elif current_menu == "SIDES":
                    menus[current_menu].append(Sides(kode,nama,harga,tingkat))

    # Menjalankan GUI
    window = tk.Tk()
    cafe = Main(window)

    window.mainloop()

if __name__ == '__main__':
    # Variabel global untuk menghubungkan setiap data pada setiap objek
    menus = {} # Menu
    temp_nama_cus = None
    temp_no_meja = None
    temp_ubah_meja = None
    pesanan = None
    total_harga = None
    # Membuat objek meja sesuai dengan no meja
    meja = [Meja(x) for x in range(10)]
    main() # Menjalankan fungsi utama