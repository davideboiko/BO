
"""""
def F1(t, F1):
    r = []
    for c in t:
        if c.isalpha():
            o = ord('A') if c.isupper() else ord('a')
            r.append(chr((ord(c) - o + F1) % 26 + o))
        else:
            r.append(c)
    return ''.join(r)

print(F1("synt{7u3_134f7_p4a_j4gpu_7u3_s10j_j4ea3!}", 13))


p:str = "flag{7=28LROT47>cD<d0>_Cb0f9c?0=bEEbCdN}"

print(p.lower())

def aggiungi_spazi(s):
    return ' '.join([s[i:i+8] for i in range(0, len(s), 8)])

# Esempio di utilizzo
numeri = "010011100111101000110000011110010100111101000101011110000101001101010100001100010101000100110000010011100111101000110101011010100101001001000100011110000110101101001101010001000011010101100110010100010011001001001001011101110101101001101010011011000110101001010000011110100100000100111001010110010110101101010110010001100101100101101011010011100110101101010100011001110011110100111101"
risultato = aggiungi_spazi(numeri)
print(risultato)


def brute_force_xor(hex_message):
    message_bytes = bytes.fromhex(hex_message)
    for key in range(1, 256):  # Provare tutte le chiavi singole (1 byte)
        decoded = ''.join(chr(b ^ key) for b in message_bytes)
        if "flag{" in decoded:
            return decoded
    return "Nessun risultato trovato."

# Prova
hex_message = "1a7e7a751c5f1d75441a5e7558194b1b1b53"
decoded_message = brute_force_xor(hex_message)
print(f"Risultato: {decoded_message}")

def xor(a, b):
    return bytes([x^y for x,y in zip(a,b)])

m1 = "158bbd7ca876c60530ee0e0bb2de20ef8af95bc60bdf" 
m2 = "73e7dc1bd30ef6576f883e79edaa48dcd58e6aa82aa2"

print(xor())
"""""


v = [0xe2, 0x50, 0x00, 0xcb, 0xc6, 0x77, 0x20, 0x7b, 0x5c, 0x6e, 0xf5, 0x5a, 0xd4, 0x2a, 0xab, 0x1b]
  
for i in range(1,256):
    for c in v:
        print(chr(c ^ i), end="")
    print()