import hashlib
# Messaggio da hashare
msg = 'hash_me_pls'.encode()

# Calcolo dell'hash SHA3-384
hash_sha3_384 = hashlib.sha3_384(msg).hexdigest()
print(hash_sha3_384)


import hmac

# Chiave e messaggio
key = bytes.fromhex('808e3a8af7f11d203f67120220d2cec0e12d4489908ac2492ab6dd811cf4ebfa')
msg = 'La mia integrità è importante!'.encode()

# Calcolo dell'HMAC con SHA-224
hmac_sha224 = hmac.new(key, msg, hashlib.sha224).hexdigest()
print(hmac_sha224)
