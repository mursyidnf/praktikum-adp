print("MURSYID NUR FAHMI")
print("2310432024\n")
def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  
            shifted_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a')) if char.islower() else chr(((ord(char.lower()) - ord('A') + shift) % 26) + ord('A'))
            encrypted_text += shifted_char
        else:
            encrypted_text += char  
    return encrypted_text

k = int(input("Bro, coba masukin angka k (1 sampe 26): "))
text = input("Masukin teks yang mau dienkripsi nih: ")

encrypted_text = caesar_cipher(text, k)
print("Ini teks yang udah dienkripsikan bro:", encrypted_text)