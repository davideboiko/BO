# Calcolo della chiave pubblica e cifratura del messaggio

# Parametri
p = 27795989555654622353
q = 33808550944382579633
e = 65537

# Calcolo del modulo n
n = p * q

# Messaggio da cifrare
message = "Adleman"

# Conversione in intero
message_int = int.from_bytes(message.encode('utf-8'), byteorder='big')

# Cifratura RSA
ciphertext = pow(message_int, e, n)

# Stampa del risultato
print("Messaggio in chiaro (intero):", message_int)
print("Messaggio cifrato:", ciphertext)
