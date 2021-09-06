import socket
import hashlib

msg=input("Enter Message :\t")
msghash=hashlib.md5(msg.encode()).hexdigest()

s=socket.socket()
print("socket created")

host=socket.gethostname()
port=12345

s.connect((host,port))
print(f"connected to {host}")


while True:
    s.send(msg.encode())
    print(" Message sent to server")
    s.send(msghash.encode())
    print(" Hash sent to server")

    ans=s.recv(1024).decode()
    print(ans)
    s.close()
    break
