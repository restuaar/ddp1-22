# Restu Ahmad Ar Ridho
# NPM : 2206028951
# TP2

# Melakukan import untuk library yang diperlukan
import os
from sys import argv

def wildcard(pattern: str) -> str:
    """
    Fungsi ini digunakan untuk mengecek pattern input, apakah pattern wildcard
    atau bukan dan mengembalikan dua nilai string hasil dari pecahan pattern
    """
    temp_index = pattern.find("*") # Mengecek apakah pattern memiliki "*" yang berarti pattern adalah wildcard
    if pattern.count("*") > 1: # Jika memiliki "*" lebih dari 1 maka input salah
        raise TypeError
    if temp_index != -1: # Melakukan slicing jika pattern adalah wildcard
        if temp_index == 0:
            pattern1 = pattern[temp_index+1:]
            pattern2 = ""
        elif temp_index+1 == len(pattern):
            pattern1 = pattern[0:temp_index]
            pattern2 = ""
        else:
            pattern1 = pattern[0:temp_index]
            pattern2 = pattern[temp_index+1:]
    else:
        pattern1 = pattern
        pattern2 = ""
    return pattern1,pattern2

def print_line(line:str,path:str,counter:int):
    """
    Fungsi ini berfungsi untuk mencetak line ke terminal
    """
    if len(line) > 40: # Jika panjang string lebih dari 40 maka di-slicing
        line = line[0:40]
    relative_path = os.path.relpath(path,os.getcwd())
    print(f"{relative_path:<40} line {counter:<3} {line:<40}")

def find_index(line:str) -> int:
    """
    Fungsi ini berfungsi untuk mencari index yang sama dengan pattern
    dan mengembalikan dua nilai index integer
    """
    global pattern1,pattern2
    index1 = line.find(pattern1)
    index2 = line.rfind(pattern2,index1+len(pattern1))
    return index1,index2

def scan_file(path:str):
    """
    Fungsi ini berfungsi untuk memeriksa ke setiap file yang dituju sesuai path
    dan mencari substring yang sama dengan pattern sesuai dengan mode yang dipilih
    """
    global mode,pattern1,pattern2
    with open(path,"r") as open_file: # Membuka file
        line_count = 1 # Deklarasi variabel untuk menghitung baris
        for line in open_file: # Melakukan enumerate untuk setiap baris
            line = line.replace("\n","")
            if mode == "-i": # Jika mode memiliki mode case insensitive
                new_line = line.casefold()
                pattern1 = pattern1.casefold()
                pattern2 = pattern2.casefold()
                if pattern2 == "": # Membagi kasus jika pattern wildcard atau tidak
                    if pattern1 in new_line:
                        print_line(line,path,line_count)
                else: 
                    index1,index2 = find_index(new_line)
                    if index1 != -1 and index2 != -1:
                        print_line(line,path,line_count)
            elif mode == "-w": # Jika mode memiliki mode case sensitive
                if pattern2 == "": # Membagi kasus jika pattern wildcard atau tidak
                    if pattern1 in line:
                        index1 = line.find(pattern1)
                        # Mengecek apakah samping kiri dan kanan pattern adalah elemen whitespace
                        if index1 == 0 and (line[index1+len(pattern1)] == " "):
                            print_line(line,path,line_count)
                        elif (line[index1-1] == " ") and (index1+len(pattern1) == len(line)):
                            print_line(line,path,line_count)
                        elif (line[index1-1] == " ") and (line[index1+len(pattern1)] == " "):
                            print_line(line,path,line_count)
                else:
                    index1,index2 = find_index(line)
                    if index1 != -1 and index2 != -1:
                        # Mengecek apakah samping kiri dan kanan pattern adalah elemen whitespace
                        if index1 == 0 and (line[index2+len(pattern2)] == " "):
                            print_line(line,path,line_count)
                        elif (line[index1-1] == " ") and (index2+len(pattern2) == len(line)):
                            print_line(line,path,line_count)
                        elif (line[index1-1] == " ") and (line[index2+len(pattern2)] == " "):
                            print_line(line,path,line_count)
            else: # Jika tidak memasukkan mode apapun
                if pattern2 == "": # Membagi kasus jika pattern wildcard atau tidak
                    if pattern1 in line:
                        print_line(line,path,line_count)
                else:
                    index1,index2 = find_index(line)
                    if index1 != -1 and index2 != -1:
                        print_line(line,path,line_count)

            line_count += 1 # Menambahkan line agar sesuai dengan enumerate-nya
    
print()
try: # Mengecek apakah tidak ada error
    if len(argv) == 3: # Membagi kasus untuk apakah terdapat mode atau tidak
        mode = ""
        pattern = argv[1]
        directory = argv[2]
        pattern1,pattern2 = wildcard(pattern)
        
        target_dir = os.path.join(os.getcwd(),directory) # Menggabungkan folder sekarang dan tujuan direktori
        if os.path.isfile(target_dir): # Membagi kasus untuk direktori yang di tuju merupakan file atau folder
            open(target_dir)    
            scan_file(target_dir)
        elif os.path.isdir(target_dir):
            scanning = os.walk(target_dir,topdown=True)
            for paths,dirs,files in scanning:
                for file in files:
                    path = os.path.join(paths,file)
                    scan_file(path)
        else:
            open(target_dir)
        
    elif len(argv) == 4:
        mode = argv[1]
        pattern = argv[2]
        directory = argv[3]
        pattern1,pattern2 = wildcard(pattern)
        if mode == "-i" or mode == "-w": # Mengecek apakah argumen yang dimasukan sudah benar
            target_dir = os.path.join(os.getcwd(),directory) # Menggabungkan folder sekarang dan dituju
            if os.path.isfile(target_dir): # Membagi kasus apakah file atau folder
                open(target_dir)    
                scan_file(target_dir)
            elif os.path.isdir(target_dir):
                scanning = os.walk(target_dir,topdown=True)
                for paths,dirs,files in scanning:
                    for file in files:
                        path = os.path.join(paths,file)
                        scan_file(path)
            else:
                open(target_dir)
        else:
            print("Argumen program tidak benar.")

    else:
        print("Argumen program tidak benar.")

except FileNotFoundError: # Handle ketika file tidak ditemukan
    print(f"Path {directory} tidak ditemukan.")
except TypeError: # Handle ketika argumen program tidak benar
    print("Argumen program tidak benar.")