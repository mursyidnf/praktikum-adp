def tambah_pasien():
    with open("data_pasien.txt", "a") as file:
        nama = input("Nama pasien = ")
        umur = input("Umur = ")
        jenis_kelamin = input("Jenis kelamin = ")
        gol_darah = input("Golongan darah = ")
        riwayat_penyakit = input("Riwayat penyakit = ")
        obat = input("Daftar obat = ")
        file.write(f"{nama},{umur},{jenis_kelamin},{gol_darah},{riwayat_penyakit},{obat}\n")
        print("Data pasien berhasil ditambahkan.\n")

def tampilkan_pasien():
    try:
        with open("data_pasien.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("Tidak ada data pasien.\n")
            else:
                for i, line in enumerate(lines, start=1):
                    data_pasien = line.strip().split(",")
                    print(f"Pasien {i}")
                    print(f"Nama: {data_pasien[0]}")
                    print(f"Umur: {data_pasien[1]}")
                    print(f"Jenis Kelamin: {data_pasien[2]}")
                    print(f"Golongan Darah: {data_pasien[3]}")
                    print(f"Riwayat Penyakit: {data_pasien[4]}")
                    print(f"Daftar Obat: {data_pasien[5]}")
                    print()
    except FileNotFoundError:
        print("Tidak ada data pasien.\n")

def hapus_pasien():
    try:
        with open("data_pasien.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("Tidak ada data pasien untuk dihapus.\n")
            else:
                print("Data pasien:")
                for i, line in enumerate(lines, start=1):
                    data_pasien = line.strip().split(",")
                    print(f"{i}. {data_pasien[0]}")
                nomor = int(input("Pilih nomor pasien yang akan dihapus: "))
                if 1 <= nomor <= len(lines):
                    del lines[nomor - 1]
                    with open("data_pasien.txt", "w") as file:
                        file.writelines(lines)
                    print("Data pasien berhasil dihapus.\n")
                else:
                    print("Nomor pasien tidak valid.\n")
    except FileNotFoundError:
        print("Tidak ada data pasien untuk dihapus.\n")

print("1. Tambah")
print("2. Tampilkan")
print("3. Hapus")
print("4. Keluar")
pilihan = input("Pilih menu = ")

if pilihan == "1":
    tambah_pasien()
elif pilihan == "2":
    tampilkan_pasien()
elif pilihan == "3":
    hapus_pasien()
elif pilihan == "4":
    print("Keluar dari program.")
else:
    print("Pilihan tidak valid, silakan coba lagi.\n")