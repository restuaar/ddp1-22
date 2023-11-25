# Restu Ahmad Ar Ridho
# NPM : 2206028951
# Lab 10

import tkinter as tk
import tkinter.messagebox as tkmsg

class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Karung Ajaib")
        self.pack()
        self.create_widgets()

    # TODO : Lengkapi Binding Event Handler dengan buttons yang ada
    def create_widgets(self):
        self.label = tk.Label(self, text = 'Selamat datang Dek Depe di Karung Ajaib. Silahkan pilih Menu yang tersedia')
        self.btn_lihat_daftar_karung = tk.Button(self,text = "LIHAT DAFTAR KARUNG",command = self.popup_lihat_karung)
        self.btn_masukkan_item = tk.Button(self, text = "MASUKKAN ITEM", command = self.popup_add_item)
        self.btn_keluarkan_item = tk.Button(self, text = "KELUARKAN ITEM", command = self.popup_keluarkan_item)
        self.btn_exit = tk.Button(self, text = "EXIT", command = self.master.destroy)

        self.label.pack()
        self.btn_lihat_daftar_karung.pack()
        self.btn_masukkan_item.pack()
        self.btn_keluarkan_item.pack()
        self.btn_exit.pack()

    # semua item dalam karung
    def popup_lihat_karung(self):
        PopupLihatKarung(self.master)

    # menu masukkan item
    def popup_add_item(self):
        PopupAddItem(self.master)

    # menu keluarkan item
    def popup_keluarkan_item(self):
        PopupKeluarkanItem(self.master)

class PopupLihatKarung(object):
    def __init__(self,master):
        global item_list
        self.main_window = tk.Toplevel()
        self.main_window.geometry("280x200")
        self.main_window.wm_title("Lihat Karung")

        self.title = tk.Label(self.main_window, text='Daftar Karung Ajaib')
        self.nama = tk.Label(self.main_window, text='Nama Item')
        self.title.pack()
        self.nama.pack()

        # TODO: Tampilkan halaman Lihat Karung Ajaib
        item_list_ordered = sorted(item_list)
        
        for item in range(1,len(item_list_ordered)+1):
            self.item = tk.Label(self.main_window, text=f"{item}. {item_list_ordered[item-1]}")
            self.item.pack()

        self.exit_button = tk.Button(self.main_window, text="EXIT", command = self.main_window.destroy)
        self.exit_button.pack()
    
# Class Masukkan Item 
class PopupAddItem(object):
    
  def __init__(self,master):
    self.main_window = tk.Toplevel()
    self.main_window.wm_title("Masukkan item")
    self.main_window.geometry("280x100")

    # TODO: Create Widget untuk tampilan Masukkan Item
    self.title = tk.Label(self.main_window, text='Input Masukkan Item')
    # self.label = tk.Label(self.main_window, text='Nama Item')
    self.temp_container = tk.StringVar()
    self.label = tk.Label(self.main_window, text='Nama Item')
    self.input = tk.Entry(self.main_window, textvariable=self.temp_container)

    self.submit_button = tk.Button(self.main_window, text = 'Masukkan', command = self.masukkan_item)

    self.title.grid(row=0, column=1,padx=2, pady=2)
    self.label.grid(row=1, column=0, padx=2, pady=2)
    self.input.grid(row=1, column=1, padx=2, pady=2)
    self.submit_button.grid(row=2, column=1, padx=2, pady=2)

  def masukkan_item(self):
    global item_list
    if self.temp_container.get() not in item_list:
        item_list.append(self.temp_container.get())
        tkmsg.showinfo(title='Berhasil!', message=f'Berhasil memasukkan item {self.temp_container.get()}.')
    else:
        tkmsg.showwarning(title='ItemHasFound', message=f'Item dengan nama {self.temp_container.get()} sudah ada di dalam Karung Ajaib.\nItem {self.temp_container.get()} tidak bisa dimasukkan lagi')
    self.main_window.destroy()
    # TODO: Create Method untuk Masukkan Item

    
# Class Keluarkan Item
class PopupKeluarkanItem(object):
    
  def __init__(self, master):
    self.main_window = tk.Toplevel()
    self.main_window.wm_title("Keluarkan item")
    self.main_window.geometry("280x100")

    # TODO: Create Widget untuk tampilan Keluarkan Item
    self.title = tk.Label(self.main_window, text='Input Keluarkan Item')
    # self.label = tk.Label(self.main_window, text='Nama Item')
    self.temp_container = tk.StringVar()
    self.label = tk.Label(self.main_window, text='Nama Item')
    self.input = tk.Entry(self.main_window, textvariable=self.temp_container)

    self.submit_button = tk.Button(self.main_window, text = 'Ambil', command = self.keluarkan_item)

    self.title.grid(row=0, column=1,padx=2, pady=2)
    self.label.grid(row=1, column=0, padx=2, pady=2)
    self.input.grid(row=1, column=1, padx=2, pady=2)
    self.submit_button.grid(row=2, column=1, padx=2, pady=2)

  def keluarkan_item(self):
    global item_list
    # TODO: Create Method untuk Keluarkan Item
    if self.temp_container.get() in item_list:
        item_list.remove(self.temp_container.get())
        tkmsg.showinfo(title='Berhasil!', message=f'Berhasil mengeluarkan item {self.temp_container.get()}.')
    else:
        tkmsg.showwarning(title='ItemHasFound', message=f'Item dengan nama {self.temp_container.get()} tidak ditemukandi dalam karung.')
    self.main_window.destroy()


item_list = []
if __name__ == "__main__":
    root = tk.Tk()
    m=MainWindow(root)
    root.mainloop()