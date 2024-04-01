print("MURSYID NUR FAHMI")
print("2310432024\n")

tinggi = int(input("Masukkan tinggi segitiga: "))

if tinggi <= 0:
    print("Tinggi harus merupakan bilangan bulat positif.")
else:
    for i in range(1, tinggi + 1):
        print(*range(1, i + 1))
