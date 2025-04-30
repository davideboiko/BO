from itertools import cycle

# Funzione per decifrare Vigenère
def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_cycle = cycle(key)  # Ripete la chiave ciclicamente

    for char in ciphertext:
        if char.isalpha():  # Solo lettere subiscono la cifratura
            shift = ord(next(key_cycle)) - ord('A')  # Shift basato sulla chiave
            shift_base = ord('A') if char.isupper() else ord('a')
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Mantiene numeri e simboli invariati

    return decrypted_text

# Supponiamo che la chiave sia "PzuurYidsitk" estratta dal testo
key = "PzuurYidsitk".upper()  # Convertiamo in maiuscolo per la decodifica
ciphertext = "Mguurq0IsigtutrvtlzK1lvnv10"

# Decifriamo il testo
print(vigenere_decrypt(ciphertext, key))
