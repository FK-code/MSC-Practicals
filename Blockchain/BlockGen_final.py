from hashlib import sha256
from datetime import datetime


class Block:
    def __init__(self,index,data,timestamp,previous_hash):
        self.index=index
        self.data=data
        self.timestamp=timestamp
        self.previous_hash=previous_hash
        nonce,hash=self.get_hash()
        self.nonce=nonce
        self.hash=hash

    def add_block(index,data):
        index=index
        data=data
        timestamp=datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        previous_hash="0"*64
        return Block(index,data,timestamp,previous_hash)

    def get_hash(self):
        Nonce=0
        diff=4
        found=False
        while found is False:
            header_bin=(
                str(self.index)+
                str(self.data)+
                str(self.timestamp)+
                str(self.previous_hash)+
                str(Nonce)
            )
            hash =sha256(header_bin.encode()).hexdigest()
            if hash[:diff]=='0'*diff:
                found=True
            Nonce+=1
        return Nonce, hash


Block_1=Block.add_block(0,"this is data")
print("Index: %s" % Block_1.index)
print("Data: %s" % Block_1.data)
print("Time: %s" % Block_1.timestamp)
print("Nonce: %s" % Block_1.nonce)
print("Previous Hash: %s" % Block_1.previous_hash)
print("Current Hash: %s" % Block_1.hash)
