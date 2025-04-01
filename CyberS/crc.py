def rot_n(text, n):
    result = ""
    for char in text:
        if 'A' <= char <= 'Z':  # Lettere maiuscole
            result += chr((ord(char) - ord('A') + n) % 26 + ord('A'))
        elif 'a' <= char <= 'z':  # Lettere minuscole
            result += chr((ord(char) - ord('a') + n) % 26 + ord('a'))
        elif '0' <= char <= '9':  # Numeri (opzionale, se ROT5)
            result += chr((ord(char) - ord('0') + n) % 10 + ord('0'))
        else:
            result += char  # Mantiene i caratteri speciali inalterati
    return result

cipher_text = input("Inserisci il testo cifrato: ")

for i in range(1, 51):  # Prova tutte le rotazioni da 1 a 50
    print(f"ROT{i}: {rot_n(cipher_text, i)}")
