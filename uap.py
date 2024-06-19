from termcolor import colored, cprint
import time
import os

# Data Peserta
data_peserta = []

# Data Kuis
kuis_data = [
    {
        "pertanyaan": "Jika |x|<3+|x-3|,maka...", 
        "pilihan": ["a. 0<x<3", "b. x<3", "c. x>3", "d. x<01"], 
        "jawaban": "b"
    },
    {
        "pertanyaan": "If it...., we will stay at home", 
        "pilihan": ["a. rains", "b. will rain", "c. rained", "d. rain"], 
        "jawaban": "a"
    },
    {
        "pertanyaan": "Hukum zakat?", 
        "pilihan": ["a. Sunnah", "b. Mubah", "c. Fardhu kifayah", "d. Wajib"], 
        "jawaban": "d"
    },
    {
        "pertanyaan": "Huruf keempat dalaam abjad?",
        "pilihan": ["a. Huruf d", "b. Huruf a", "c. Tidak tau", "d. Salah semua"],
        "jawaban": "b"
    },
    {
        "pertanyaan": "Persamaan teori Lamark dan Darwin tentang faktor yang menentukan arah evolusi?",
        "pilihan": ["a. Seleksi bertahun-tahun pada suatu individu", "b. Perubahan lingkungan orgaisme", "c. variasi genetik", "d. Mutasi"],
        "jawaban": "b"
    },
    {
        "pertanyaan": "Jumlah pulau di Indonesia?",
        "pilihan": ["a. 1000", "b. 6", "c. 17.001", "d. 38"],
        "jawaban": "c"
    },
    {
        "pertanyaan": "Macam-macam ideologi?",
        "pilihan": ["a. Sosialisme", "b. Komunisme", "c. Liberal", "d. Semua benar"],
        "jawaban": "d"
    },
    {
        "pertanyaan": "1+1x0=",
        "pilihan": ["a. 1", "b. 0", "c. -1", "d. 2"],
        "jawaban": "a"
    },
    {
        "pertanyaan": "Sinonim dari sengketa adalah....",
        "pilihan": ["a. Konformitas", "b. Konfrontasi", "c. Konkurensi", "d. Obligasi"],
        "jawaban": "c"
    },
    {
        "pertanyaan": "Susunan elektron valensi gas mulia yang tidak oktet adalah....",
        "pilihan": ["a. Xe", "b. Ar", "c. Ne", "d. He"],
        "jawaban": "d"
    }
]

# Animasi time to kuis
def animasi_awal():
    for i in range(3):
        cprint(" KUIS " * 5, 'white', 'on_red')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

        cprint(" KUIS " * 5, 'white', 'on_yellow')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

        cprint(" KUIS " * 5, 'white', 'on_green')
        time.sleep(0.5)
        os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk animasi hitungan mundur
def animasi_hitungan_mundur():
    for i in range(3, 0, -1):
        print(colored(f"{i}", 'cyan'))
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk animasi mulai kuis
def animasi_mulai_kuis():
    print(colored("Kuis dimulai!", 'cyan'))
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi untuk animasi jawaban benar
def animasi_jawaban_benar():
    for i in range(3):  
        print(colored("Jawaban Benar!", 'green'))  
        time.sleep(0.2)  
        os.system('cls' if os.name == 'nt' else 'clear')   
        time.sleep(0.3)  

# Fungsi untuk animasi jawaban salah
def animasi_jawaban_salah():
    for i in range(3):  
        print(colored("Jawaban Salah!", 'red'))  
        time.sleep(0.2)  
        os.system('cls' if os.name == 'nt' else 'clear')  
        time.sleep(0.3)

# Fungsi untuk menampilkan skor
def skor(jumlah_benar, total_pertanyaan):
    return f"{jumlah_benar}/{total_pertanyaan}"

# Fungsi utama kuis
def kuis():
    animasi_hitungan_mundur()  # Panggil animasi hitungan mundur sebelum mulai kuis
    animasi_mulai_kuis()       # Panggil animasi mulai kuis setelah hitungan mundur
    pertanyaan = 0
    jumlah_benar = 0

    while pertanyaan < len(kuis_data):
        print(colored(kuis_data[pertanyaan]['pertanyaan'], 'blue'))
        
        for pilihan in kuis_data[pertanyaan]['pilihan']:
            print(colored(pilihan, 'yellow'))
        
        jawaban = input("Pilih jawaban (a/b/c/d): ").strip().lower()

        if jawaban == kuis_data[pertanyaan]['jawaban']:
            animasi_jawaban_benar()
            jumlah_benar += 1
        else:
            animasi_jawaban_salah()

        # Jeda sejenak sebelum pertanyaan berikutnya
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')

        pertanyaan += 1

    print(colored("Kuis Selesai!", 'yellow'))
    return jumlah_benar

# Menampilkan animasi awal
animasi_awal()

# Menu
while True:
    print(colored("Menu", 'green'))
    print("1. Isi data peserta")
    print("2. Mulai kuis")
    print("3. Tampilkan semua data peserta")
    print("4. Keluar")
    pilihan = input("Pilih menu = ")

    if pilihan == "1":
        nama = input("Masukkan nama peserta: ")
        NIM = input("Masukkan NIM peserta: ")
        data_peserta.append({"nama": nama, "NIM": NIM, "skor": None})
        print(colored("Data peserta berhasil ditambahkan!\n", 'green'))

    elif pilihan == "2":
        if data_peserta:
            print(colored("Mulai Kuis untuk peserta terakhir.\n", 'cyan'))
            jumlah_benar = kuis()
            data_peserta[-1]["skor"] = skor(jumlah_benar, len(kuis_data))
        else:
            print(colored("Tidak ada peserta yang terdaftar. Silakan tambahkan peserta terlebih dahulu.\n", 'red'))

    elif pilihan == "3":
        os.system('cls' if os.name == 'nt' else 'clear')  # Bersihkan layar sebelum menampilkan data
        if data_peserta:
            print(colored("Data Semua Peserta:", 'cyan'))
            for idx, peserta in enumerate(data_peserta, start=1):
                print(f"{idx}. Nama: {peserta['nama']}, NIM: {peserta['NIM']}, Skor: {peserta['skor']}")
        else:
            print(colored("Belum ada data peserta.\n", 'red'))

    elif pilihan == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(colored("Keluar dari program.", 'red'))
        break

    else:
        print(colored("Pilihan tidak valid, silakan coba lagi.\n", 'red'))