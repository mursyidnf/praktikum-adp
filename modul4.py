print("MURSYID NUR FAHMI")
print("2310432024\n")

def faktor_bilangan(n):
    faktor = [i for i in range(1, n) if n % i == 0]
    return faktor

def cek_bilangan_sempurna(n):
    return sum(faktor_bilangan(n)) == n

bilangan = int(input("Masukkan bilangan bulat positif: "))

if bilangan <= 0:
    print("Bilangan harus positif!")
else:
    print(f"Faktor dari {bilangan}: {faktor_bilangan(bilangan)}")
    if cek_bilangan_sempurna(bilangan):
        print(f"{bilangan} adalah bilangan sempurna.")
    else:
        print(f"{bilangan} bukan bilangan sempurna.")