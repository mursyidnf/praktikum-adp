print("")
print("MURSYID NUR FAHMI")
print("2310432024")
print("")

menu_makanan = {
    1: {"nama": "Nasi Goreng", "harga": 10000},
    2: {"nama": "Minas", "harga": 12000},
    3: {"nama": "Bakso", "harga": 18000},
    4: {"nama": "Ayam Goreng", "harga": 25000},
}

menu_minuman = {
    1: {"nama": "Es Teh Manis", "harga": 5000},
    2: {"nama": "Kopi", "harga": 4000},
    3: {"nama": "Susu", "harga": 3000},
    4: {"nama": "Jus Jeruk Nipis", "harga": 7000},
    5: {"nama": "Air Mineral", "harga": 4000},
}

def pesan_makanan():
    print("Menu Makanan:")
    for kode, item in menu_makanan.items():
        print(f"{kode}. {item['nama']} - Rp {item['harga']}")

    kode_pesanan = int(input("Silakan pilih kode makanan yang ingin dipesan: "))
    jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))

    item = menu_makanan.get(kode_pesanan)
    if item:
        total_harga = item['harga'] * jumlah_pesanan
        print(f"Anda telah memesan {item['nama']} sebanyak {jumlah_pesanan} dengan total harga Rp {total_harga}")
        return total_harga
    else:
        print("Kode pesanan makanan tidak valid")
        return 0

def pesan_minuman():
    print("Menu Minuman:")
    for kode, item in menu_minuman.items():
        print(f"{kode}. {item['nama']} - Rp {item['harga']}")

    kode_pesanan = int(input("Silakan pilih kode minuman yang ingin dipesan: "))
    jumlah_pesanan = int(input("Masukkan jumlah pesanan: "))

    item = menu_minuman.get(kode_pesanan)
    if item:
        total_harga = item['harga'] * jumlah_pesanan
        print(f"Anda telah memesan {item['nama']} sebanyak {jumlah_pesanan} dengan total harga Rp {total_harga}")
        return total_harga
    else:
        print("Kode pesanan minuman tidak valid")
        return 0

def pesan_makanan_dan_minuman():
    total_harga_makanan = pesan_makanan()
    total_harga_minuman = pesan_minuman()
    total_harga = total_harga_makanan + total_harga_minuman
    print(f"Total harga keseluruhan: Rp {total_harga}")
    print("Semoga anda puas dengan menu kedai ini, Selamat Datang Kembali :)")
    print("")

def main():
    print("Selamat datang di program Kedai Mursyid")
    print("Jenis Pesanan:")
    print("1. Makanan")
    print("2. Minuman")
    print("3. Makanan dan Minuman")

    jenis_pesanan = int(input("Silakan pilih jenis pesanan (1/2/3): "))

    if jenis_pesanan == 1:
        pesan_makanan()
    elif jenis_pesanan == 2:
        pesan_minuman()
    elif jenis_pesanan == 3:
        pesan_makanan_dan_minuman()
    else:
        print("Kode Pesanan Tidak Valid")

if __name__ == "__main__":
    main()