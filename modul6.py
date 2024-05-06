print("MURSYID NUR FAHMI")
print("2310432024\n")
def tampilkan_jadwal_penerbangan(jadwal_penerbangan):
    print("Jadwal Penerbangan:")
    print("{:<15} {:<10} {:<10} {:<20} {:<20}".format("No. Penerbangan", "Dari", "Ke", "Waktu Keberangkatan", "Waktu Kedatangan"))
    for penerbangan in jadwal_penerbangan:
        print("{:<15} {:<10} {:<10} {:<20} {:<20}".format(*penerbangan))

def cari_rute_tercepat(jadwal_penerbangan, asal, tujuan):
    rute_tercepat = None
    durasi_tercepat = float('inf')

    for penerbangan in jadwal_penerbangan:
        if penerbangan[1] == asal and penerbangan[2] == tujuan:
            durasi = penerbangan[4] - penerbangan[3]
            if durasi < durasi_tercepat:
                durasi_tercepat = durasi
                rute_tercepat = penerbangan

    return rute_tercepat

jadwal_penerbangan = [
    ["ABC123", "Padang", "Jakarta", 800, 917],
    ["XYZ456", "Padang", "Jakarta", 1200, 1655],
    ["DEF789", "Padang", "Jakarta", 1710, 1850]
]

tampilkan_jadwal_penerbangan(jadwal_penerbangan)

asal_kota = "Padang"
tujuan_kota = "Jakarta"
rute_tercepat = cari_rute_tercepat(jadwal_penerbangan, asal_kota, tujuan_kota)

if rute_tercepat:
    print("\nRute Tercepat dari {} ke {}:".format(asal_kota, tujuan_kota))
    print("No. Penerbangan: ", rute_tercepat[0])
    print("Dari: ", rute_tercepat[1])
    print("Ke: ", rute_tercepat[2])
    print("Waktu Keberangkatan: ", rute_tercepat[3])
    print("Waktu Kedatangan: ", rute_tercepat[4])
else:
    print("\nTidak ada penerbangan langsung dari {} ke {}.".format(asal_kota, tujuan_kota))