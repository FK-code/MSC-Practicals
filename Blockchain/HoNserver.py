import socket
import hashlib

s=socket.socket()
print(" socket created")

host=socket.gethostname()
port=12345
s.bind((host,port))
print(f" socket binded to \t {port}")
s.listen()
try:
    while True:
        clt,adr=s.accept()
        print(f" Connected to \t {adr}")

        msg=clt.recv(1024).decode()
        print(f" Message received {msg}")

        msghash=clt.recv(1024).decode()
        print(f" Hash received {msghash}")

        hashgen=hashlib.md5(msg.encode()).hexdigest()
        if hashgen==msghash:
            ans=" Hash matches \n Message integrity is maintained"
            clt.send(ans.encode())
            print(ans)
        else:
            ans=" Hash does not match \n Message integrity is lost"
            clt.send(ans.encode())
            print(ans)
        clt.close()
        break
       
except Exception as e:
    print(e)