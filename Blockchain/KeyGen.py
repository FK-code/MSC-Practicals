# from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes

## from Crypto.PublicKey import RSA

# secret_code = "Unguessable"
# key = RSA.generate(2048)
# encrypted_key = key.export_key(passphrase=secret_code, pkcs=8,protection="scryptAndAES128-CBC")
# print(len(encrypted_key))
## print(encrypted_key)

# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_EAX)

#print(len(cipher))
# print(cipher)

import base64
import ecdsa

def generate_vapid_keypair():
  """
  Generate a new set of encoded key-pair for VAPID
  """
  pk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
  vk = pk.get_verifying_key()

  return {
    'private_key': base64.urlsafe_b64encode(pk.to_string()).strip("="),
    'public_key': base64.urlsafe_b64encode("\x04" + vk.to_string()).strip("=")
  }

from ecdsa import SigningKey
private_key = SigningKey.generate() # uses NIST192p
signature = private_key.sign(b"Educative authorizes this shot")
print(signature)
public_key = private_key.verifying_key
print("Verified:", public_key.verify(signature, b"Educative authorizes this shot"))

#TODO 2 sysmetric key algo 2 asysmetric key algo
