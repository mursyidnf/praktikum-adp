print("MURSYID")
print("2310432024")

def multiplication_table(n):
    print("\nTabel Perkalian:")
    print("    ", end="")
    for i in range(1, n + 1):
        print("{:4d}".format(i), end="")
    print("\n" + "-" * (5 * n + 4))
    for i in range(1, n + 1):
        print("{:2d} |".format(i), end="")
        for j in range(1, n + 1):
            print("{:4d}".format(i * j), end="")
        print()

def addition_table(n):
    print("\nTabel Penjumlahan:")
    print("    ", end="")
    for i in range(1, n + 1):
        print("{:4d}".format(i), end="")
    print("\n" + "-" * (5 * n + 4))
    for i in range(1, n + 1):
        print("{:2d} |".format(i), end="")
        for j in range(1, n + 1):
            print("{:4d}".format(i + j), end="")
        print()

def main():
    while True:
        print("\nSILAHKAN PILIH MENU SATU, DUA ATAU TIGA")
        print("\nMENU :")
        print("1. Tabel Perkalian n x n")
        print("2. Tabel Penjumlahan n x n")
        print("3. Keluar")
        
        choice = input("\nPilih menu (1/2/3): ")

        if choice == '1':
            n = int(input("\nMasukkan nilai n (1-10): "))
            if 1 <= n <= 10:
                multiplication_table(n)
            else:
                print("Masukkan nilai n antara 1 hingga 10.")
        elif choice == '2':
            n = int(input("\nMasukkan nilai n (1-10): "))
            if 1 <= n <= 10:
                addition_table(n)
            else:
                print("Masukkan nilai n antara 1 hingga 10.")
        elif choice == '3':
            print("SEMANGAT TERUS BELAJARNYA YAAA ^^")
            print("")
            break
        else:
            print("\nPilihan tidak valid. Masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    main()