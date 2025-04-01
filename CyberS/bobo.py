import base64


"""""

ex_string = "627062637b676278186a3530263031272124292f2b103c163b750d2272393f595d12435d5458581849130d000101034c120218015e0a30485c3a54431f154636035a1d311a501a4706561b5f144454125a5a155b585c5641121101060f435e5e544140415b57174e58130b021e0c09020447150b594e2f09423e19561902597f025a1e3a05111d5a47521b5d12105012424150454357190c0d0e010b125f4444464751155a52185a0e0f160a0c050d1b0e1400594e2c075e3054471f1143321540013a53111d47155504560f435e12465a15555656580d0743170c0545435d575d5b13555253594c5041010c0a03031e0c061501100d370d103e17500803433050571b2f161e0d564750135f5d535e4041514142581849130d0001010f5d545c475f595f545c4658574d51560f0b4307170f180804130b101c3a1b443e1a5c4d13452c045c163607154950085917130e4450505a585c4258185d000e0f01451455565d5f555e5e5c13515853455f560f0d43050b0901000b120b10003a01102f015d1919103b191311301d041b5c0b581d131955425b545a54425e435e5e47555b425818550042000c0c071a044718015e1d3a06443a54570450463a1456003a5313005c47571a565d5f4353135954585459514546565a515f56555641010c0a03031e0c065b1e42073209103b1d130c0651310a52003a5313065d475d1e130d425e41405d585917485812110c"

# Convertire la stringa esadecimale in bytes
byte_data = bytes.fromhex(hex_string)

# Tentare di decodificare in formato ASCII
try:
    decoded_text = byte_data.decode('utf-8', 'ignore')
    print(decoded_text)
except UnicodeDecodeError as e:
    decoded_text = f"Errore nella decodifica: {e}"

print(decoded_text)

"""""

def decode_base64(encoded_string):
    try:
        # Decodifica la stringa da Base64
        decoded_bytes = base64.b64decode(encoded_string)
        # Converte i byte in una stringa leggibile
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string
    except Exception as e:
        # Gestisce eventuali errori
        return f"Errore durante la decodifica: {e}"

# Esempio di utilizzo
if __name__ == "__main__":
    # Inserisci qui la tua stringa codificata in Base64
    encoded_input = input("Inserisci la stringa codificata in Base64: ")
    result = decode_base64(encoded_input)
    print(f"Risultato decodificato: {result}")



    data = [0xb2, 0x30, 0xbd, 0xdc, 0x10, 0x7a, 0xe1, 0x7b, 0x2c, 0x3b, 0xe2, 0xec, 0x99, 0x01]
key = 0x55  # esempio di chiave
decoded = [byte ^ key for byte in data]
print(''.join(chr(b) for b in decoded))
