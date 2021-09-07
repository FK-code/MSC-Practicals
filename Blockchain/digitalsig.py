from ecdsa import SigningKey

msg="Hello World"
private_key = SigningKey.generate() 
signature = private_key.sign(msg.encode())
print(signature)
public_key = private_key.verifying_key
print(public_key)
print("Verified:", public_key.verify(signature, msg.encode()))

