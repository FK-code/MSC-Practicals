import hashlib
from hashlib import sha512
from Crypto.PublicKey import RSA

keyPair = RSA.generate(bits=1024)
print(f"Public key:  (n={hex(keyPair.n)}, e={hex(keyPair.e)})")
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

def hashing(data):
    hash_code = hashlib.sha256(data.encode())
##    h=hash_code.hexdigest()
    print("Your message: ",data)
##    print("The hexadecimal equivalent of hash is : ",h)

def encrypt(hash_code):
    signature = pow(int.from_bytes(hash_code,byteorder='big'), keyPair.d, keyPair.n)
    print("Signature:", signature)

def decrypt(data,signature):
    data_hash=hashing(data)
    hashFromSignature = pow(signature, keyPair.e, keyPair.n)
    print("Signature valid:", hashFromSignature)
    
def check_validity(h,hashFromSignature):
    if h==hashFromSignature:
        print("valid")
    else:
        print("not valid")

data=input(b'message: ')
hash_code=hashing(data)
cipher=encrypt(hash_code)
print(cipher)
plaintext=decrypt(data,signature)
print(plaintext)
check_validity(hash_code,plaintext)
