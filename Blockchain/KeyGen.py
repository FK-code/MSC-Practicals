#TODO 2 sysmetric key algo 2 asysmetric key algo

#symmetric key gen key key len
# AES DES Blowfish RC4 RC5 RC6 HmacMD5 HmacSHA1
# #asymmetric key
# RSA DSA ECC 

data="Hello world Data"
# RSA
from Crypto.PublicKey import RSA

key=RSA.generate(1024)
private_key=key.exportKey("PEM")
public_key=key.publickey().exportKey("PEM")
print("RSA Public Key : \n")
print(public_key.decode())
print("")
print(f"Length of Public Key : {len(public_key)}")
print("")
print(private_key.decode())
print("")
print(f"Length of Public Key : {len(private_key)}")


# DSA
from Crypto.PublicKey import DSA

key=DSA.generate(1024)
public_key=key.publickey().exportKey()
private_key=key.exportKey()
print("DSA Public Key : \n")
print(public_key.decode())
print("")
print(f"Length of Public Key : {len(public_key)}")
print("")
print(private_key.decode())
print("")
print(f"Length of Public Key : {len(private_key)}")

# AES
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key=get_random_bytes(16)
cipher = AES.new(key, AES.MODE_EAX)

print(f"Key from AES algorithm in hex format: \n {cipher.hexdigest()}")

#DES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key=get_random_bytes(8)
cipher =DES.new(key,DES.MODE_EAX)
print(f"Key from DES algorithm in hex format: \n {cipher.hexdigest()}")