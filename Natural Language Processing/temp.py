from Crypto.PublicKey import RSA
#To generate a 1024 bit RSA key-pair
keyPair = RSA.generate(bits=1024)
print(f"Public key: (n={hex(keyPair.n)}, e{hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")