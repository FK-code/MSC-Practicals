# from ecdsa import SigningKey

# msg="Hello World"
# private_key = SigningKey.generate() 

# signature = private_key.sign(msg.encode())

# print("\n private key \n")
# print(signature)

# public_key = private_key.verifying_key

# print("\n public key \n")
# print(public_key)

# print("Verified:", public_key.verify(signature, msg.encode()))


# import rsa

# data="this is data"

# private_key, public_key = rsa.newkeys(512)
# encrypted_data=rsa.encrypt(data.encode(), private_key)
# print(encrypted_data)
# plaintext=rsa.decrypt(encrypted_data, public_key).decode()
# print(plaintext)




# To generate a 1024-bit RSA key-pair
from Crypto.PublicKey import RSA
from hashlib import sha256

def sign_data(message,private_key_n,private_key_d):
    hashed_msg=sha256(message.encode()).digest()
    #for pow we need int values , convert hash byte to int
    hash=int.from_bytes(hashed_msg,byteorder='big')
    signature=pow(hash,private_key_d,private_key_n)
    print("Data signed \n")
    return hashed_msg, signature

def verify_data(public_key_n,public_key_e,hashed_msg,signature):
    # try:
        hash=int.from_bytes(hashed_msg,byteorder='big')
        hashfromsignature=pow(signature,public_key_e,public_key_n)    
        print("The signature is valid :", hash==hashfromsignature)
    # except:
    #     print("signature is not valid")

#generating private and public keys
key=RSA.generate(1024)
private_key_n=key.n
private_key_d=key.d
public_key_n=key.n
public_key_e=key.e

msg=input("Enter message to sign \t")
flag=False
while flag is False:
    c=int(input("1. Sign data 2. Verify signature  3. Exit\t Selected value : "))
    if c==1:
        hashed_data,signature=sign_data(msg,private_key_n,private_key_d)
    if c==2:
        verify_data(public_key_n,public_key_e,hashed_data,signature)
    if c==3:
        flag=True