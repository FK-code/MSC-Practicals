#TODO 2 sysmetric key algo 2 asysmetric key algo

#symmetric key gen key key len
# AES DES Blowfish RC4 RC5 RC6 HmacMD5 HmacSHA1
# #asymmetric key
# RSA DSA ECC 

data="Hello world Data"
# RSA
from Crypto.PublicKey import RSA

key=RSA.generate(1024)
private_key1=key.exportKey("PEM")
public_key1=key.publickey().exportKey("PEM")
private_key2=key.exportKey("PEM")
public_key2=key.publickey().exportKey("PEM")
print("RSA Public Key : \n")
# print(public_key.decode())
# print("")
# print(f"Length of Public Key : {len(public_key)}")
# print("")
# print(private_key.decode())
# print("")
# print(f"Length of Public Key : {len(private_key)}")

if len(public_key1)==len(public_key2):
    print("Both public keys are equal ? :  True")
else:
    print("Both public keys are equal ? :  False")

if len(private_key1)==len(private_key2):
    print("Both private keys are equal ? :  True")
else:
    print("Both private keys are equal ? :  False")


# DSA
from Crypto.PublicKey import DSA

key=DSA.generate(1024)
public_key1=key.publickey().exportKey()
private_key1=key.exportKey()
public_key2=key.publickey().exportKey()
private_key2=key.exportKey()
print("DSA Public Key : \n")
# print(public_key.decode())
# print("")
# print(f"Length of Public Key : {len(public_key1)}")
# print("")
# print(private_key.decode())
# print("")
# print(f"Length of Public Key : {len(private_key1)}")

if len(public_key1)==len(public_key2):
    print("Both public keys are equal ? :  True")
else:
    print("Both public keys are equal ? :  False")

if len(private_key1)==len(private_key2):
    print("Both private keys are equal ? :  True")
else:
    print("Both private keys are equal ? :  False")


# AES
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

key=get_random_bytes(16)
print(f"Random bytes passed : \n {key}")
cipher1 = AES.new(key, AES.MODE_EAX)

cipher2=AES.new(key,AES.MODE_EAX)
print(f"Key from AES algorithm in hex format: \n {cipher1.hexdigest()}")
print(f"Key from AES algorithm in hex format: \n {cipher2.hexdigest()}")
if len(cipher1.hexdigest()) == len(cipher2.hexdigest()):
    print("Both keys are equal ? :  True")
else:
    print("Both keys are equal ? :  False")


#DES
from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

key=get_random_bytes(8)
print(f"Random bytes passed : \n {key}")
cipher1 =DES.new(key,DES.MODE_EAX)
cipher2=DES.new(key,DES.MODE_EAX)
print(f"Key from DES algorithm in hex format: \n {cipher1.hexdigest()}")
print(f"Key from DES algorithm in hex format: \n {cipher2.hexdigest()}")
if len(cipher1.hexdigest()) == len(cipher2.hexdigest()):
    print("Both keys are equal ? :  True")
else:
    print("Both keys are equal ? :  False")
