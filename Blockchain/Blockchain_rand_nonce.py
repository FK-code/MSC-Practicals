import hashlib
from datetime import datetime
from random import randint

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
        block=Block(self.index,"Genesis Block","None")
        self.chain.append(block)


class Block():
    def __init__(self,index,data,prev_hash):
        self.index=index
        self.data=data
        self.nonce=randint(1000,9999)
        self.time=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        self.prev_hash=prev_hash
        self.curr_hash=self.get_hash()

    def get_hash(self):
        string=(
            str(self.index)+
            str(self.data)+
            str(self.nonce)+
            str(self.prev_hash)
        )
        hash=hashlib.sha256(string.encode()).hexdigest()
        return hash

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
    ch=int(input("1. View Blockchain 2. Add block 3. Blockchain Lenght 4. Exit \t"))
    if ch==1:
        print_blockchain()
    if ch==2:
        data=input("Enter data to be inserted in block \t")
        blockchain.add_block(data)
    if ch==3:
        print("Blockchain lenght",len(blockchain.chain))
    if ch==4:
        flag = False





# print("Block 1: ", blockchain.chain[0].index)
# print("Block 1: ", blockchain.chain[0].data)
# print("Block 2: ", blockchain.chain[1].index)
# print("Block 2: ", blockchain.chain[1].data)
        
