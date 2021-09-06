from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

from Crypto.PublicKey import RSA

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,protection="scryptAndAES128-CBC")
print(len(encrypted_key))
print(encrypted_key)

# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_EAX)

#print(len(cipher))
# print(cipher)
