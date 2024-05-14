print("MURSYID NUR FAHMI")
print("2310432024\n")

def jadwal_saya():
    jadwal_harian = []
    while True:
        print("Menu:")
        print("1. Tambah kegiatan")
        print("2. Hapus kegiatan")
        print("3. Tampilkan jadwal")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            jumlah_kegiatan = int(input("Jumlah kegiatan: "))
            for _ in range(jumlah_kegiatan):
                waktu_mulai = input("Waktu mulai : ")
                waktu_selesai = input("Waktu selesai : ")
                deskripsi = input("Deskripsi: ")
                jadwal_harian.append((waktu_mulai, waktu_selesai, deskripsi))
        elif pilihan == "2":
            deskripsi = input("Kegiatan yg dihapus: ")
            jadwal_harian[:] = [kegiatan for kegiatan in jadwal_harian if kegiatan[2] != deskripsi]
            print("Kegiatan berhasil dihapus!")
        elif pilihan == "3":
            if not jadwal_harian:
                print("Jadwal harian kosong.")
            else:
                print("Jadwal Harian:")
                for index, kegiatan in enumerate(jadwal_harian, start=1):
                    print(f"{index}. Waktu: {kegiatan[0]} - {kegiatan[1]}, Deskripsi: {kegiatan[2]}")
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid.")
jadwal_saya()