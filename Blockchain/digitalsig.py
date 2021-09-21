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


import rsa

data="this is data"

private_key, public_key = rsa.newkeys(512)
encrypted_data=rsa.encrypt(data.encode(), private_key)
print(encrypted_data)
plaintext=rsa.decrypt(encrypted_data, public_key).decode()
print(plaintext)
