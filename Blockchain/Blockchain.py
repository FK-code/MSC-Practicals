import hashlib
from datetime import datetime

# block data limit 1 item

class Blockchain():
    def __init__(self):
        self.chain=[]
        self.gen=self.add_genesis_block()

    def add_block(self,data):
        self.index=len(self.chain)
        prev_hash=self.chain[self.index-1].curr_hash
        block=Block(self.index,data,prev_hash)
        self.chain.append(block)

    def add_genesis_block(self):
        self.index=len(self.chain)
        block=Block(self.index,"Genesis Block",self.get_initial_hash())
        self.chain.append(block)

    def get_initial_hash(self):
        nonce=1
        diff=2
        found=False
        while found is False:
            empty_hash=hashlib.sha256(str(nonce).encode()).hexdigest()
            if empty_hash[:diff] =='0'*diff:
                found=True
            nonce+=1
        return empty_hash

class Block():
    def __init__(self,index,data,prev_hash):
        self.index=index
        self.data=data
        self.prev_hash=prev_hash
        nonce,hash=self.get_hash()
        self.nonce=nonce
        self.time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.curr_hash=hash

    def get_hash(self):
        Nonce=0
        diff=2
        found=False
        while found is False:
            string=(
                str(self.index)+
                str(self.data)+
                str(Nonce)+
                str(self.prev_hash)
            )
            hash=hashlib.sha256(string.encode()).hexdigest()
            if hash[:diff]=='0'*diff:
                found=True
            Nonce+=1
        return Nonce, hash

blockchain=Blockchain()

def print_blockchain():
    for i in range(0,len(blockchain.chain)):
        print("\nBlock No : ",i)
        print("Index : ",blockchain.chain[i].index)
        print("Data : ",blockchain.chain[i].data)
        print("Nonce : ",blockchain.chain[i].nonce)
        print("Time : ",blockchain.chain[i].time)
        print("Prev Hash : "+blockchain.chain[i].prev_hash)
        print("Curr Hash : "+blockchain.chain[i].curr_hash+"\n")


flag = True
while flag:
    ch=int(input("1. View Blockchain 2. Add block 3. Blockchain Length 4. Exit \t"))
    if ch==1:
        print_blockchain()
    if ch==2:
        data=input("Enter data to be inserted in block \t")
        blockchain.add_block(data)
    if ch==3:
        print("Blockchain length : ",len(blockchain.chain))
    if ch==4:
        flag = False

# rasikamundhe@ruiacollege.edu