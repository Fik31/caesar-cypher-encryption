# FIKRIAN NUR ABDULLAH 15220611

def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Periksa apakah karakter adalah huruf
            offset = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Jika bukan huruf, tidak diubah
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Periksa apakah karakter adalah huruf
            offset = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - offset - shift) % 26 + offset)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Jika bukan huruf, tidak diubah
    return decrypted_text

# Pesan asli
plain_text = "MENYALA"
shift = 3

# Enkripsi
encrypted_text = caesar_cipher_encrypt(plain_text, shift)
print("Pesan terenkripsi:", encrypted_text)

# Dekripsi
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
print("Pesan terdekripsi:", decrypted_text)


# Kode ini menggunakan pergeseran 3 untuk mengenkripsi dan mendekripsi pesan dengan algoritma Caesar Cipher. Berikut adalah hasilnya:

# Enkripsi:
# Input: "MENYALA"
# Output: "PHQBDOD" (hasil pesan terenkripsi)

# Dekripsi:
# Input: "PHQBDOD"
# Output: "MENYALA" (kembali ke pesan asli)