import hashlib
 
msg=input("Enter the message :- ")
flag="y"
while flag=="y":
    print("Select Hashing Algorithm")
    choice=int(input(" 0) Update Message \n 1) sha3_224 \t 2) sha224 \t 3) sha3_512 \t 4) sha1 \t 5) sha512 \t 6) sha256 \t 7) sha3_384 \n 8) sha3_256 \t 9) md5 \t 10) shake_256 \t 11) blake2s \t 12) blake2b \t 13) shake_128 \t 14) sha384 \n"))
    if choice==0:
        msg=input("Enter the message :- ")
    elif choice==1:
        hash=hashlib.sha3_224(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==2:
        hash=hashlib.sha224(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==3:
        hash=hashlib.sha3_512(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==4:
        hash=hashlib.sha1(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==5:
        hash=hashlib.sha512(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==6:
        hash=hashlib.sha256(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==7:
        hash=hashlib.sha3_384(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==8:
        hash=hashlib.sha3_256(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==9:
        hash=hashlib.md5(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==10:
        hash=hashlib.shake_256(msg.encode()).hexdigest(10)
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==11:
        hash=hashlib.blake2s(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==12:
        hash=hashlib.blake2b(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==13:
        hash=hashlib.shake_128(msg.encode()).hexdigest(10)
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    elif choice==14:
        hash=hashlib.sha384(msg.encode()).hexdigest()
        print("Message : "+msg+", Equivalent hexadecimal hash : "+hash)
    else:
        print("Not a Valid option")
    
    flag=input("Continue? (y/n)").lower()    
    

