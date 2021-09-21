# class Block:
#     def __init__(self, previous_block_hash, data, timestamp,nonce):
#         self.previous_block_hash=previous_block_hash
#         self.timestamp=timestamp
#         self.data=data
#         self.nonce=nonce

        



# https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/

# from hashlib import sha256
# import json
# import time

# class Block:
#     def __init__(self,index,transactions,timestamp,previous_hash,nonce=0):
#         self.index=index
#         self.transactions=transactions
#         self.timestamp=timestamp
#         self.previous_hash=previous_hash
#         self.nonce=nonce

#     def compute_hash(self):
#         block_string=json.dumps(self.__dict__, sort_keys=True)
#         return sha256(block_string.encode()).hexdigest()

# class Blockchain:
#     def __init__(self):
#         self.unconfirmed_transactions=[]
#         self.chain=[]
#         self.create_genesis_block()

#     def create_genesis_block(self):
#         genesis_block=Block(0,[],time.time(),"0")
#         genesis_block.hash=genesis_block.compute_hash()
#         self.chain.append(genesis_block)

#     @property
#     def last_block(self):
#         return self.chain[-1]       

#     difficulty=2
#     def proof_of_work(self,block):
#         block.nonce=computed_hash=block.compute_hash()
#         while not computed_hash.startswith("0"*Blockchain.difficulty):
#             block.nonce+=1
#             computed_hash=block.compute_hash()
#         return computed_hash
    
#     def add_block(self,block,proof):
#         previous_hash=self.last_block.hash
#         if previous_hash != block.previous_hash:
#             return False
#         if not self.is_valid_proof(block,proof):
#             return False
#         block.hash=proof
#         self.chain.append(block)
#         return True
    
#     def is_valid_proof(self,block,block_hash):
#         return(block_hash.startswith("0"*Blockchain.difficulty) and block_hash == block.computed_hash())

#     def add_new_transaction(self,transaction):
#         self.unconfirmed_transactions.append(transaction)
    
#     def mine(self):
#         if not self.unconfirmed_transactions:
#             return False
#         last_block=self.last_block

#         new_block =Block(
#             index=last_block.index+1,
#             transaction=self.unconfirmed_transactions,
#             timestamp=time.time(),
#             previous_hash=last_block.hash
#         )

#         proof=self.proof_of_work(new_block)

#         self.add_block(new_block, proof)
#         self.unconfirmed_transactions=[]
#         return new_block.index

# from flask import Flask,request
# import requests

# app = Flask(__name__)
# blockchain=Blockchain()

# @app.route('/chain', methods=['GET'])
# def get_chain():
#     chain_data=[]
#     for block in blockchain.chain:
#         chain_data.append(block.__dict__)
#     return json.dumps({"length":len(chain_data),
#                         "chain":chain_data})
# app.run(port=5000)







# pending_transaction = data
# proof = nonce



# blockchain as a list, nonce manual

import hashlib
import json
from time import time



class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.data=[]

        self.new_block(previous_hash="0",nonce=100)
    
    def new_block(self,nonce,previous_hash=None):
        block={
            "index": len(self.chain) +1,
            "timestamp":time(),
            "data":self.data,
            "nonce":nonce,
            "previous_hash":previous_hash or self.hash(self.chain[-1]),
        }
        self.data=[]
        self.chain.append(block)

        return block

    @property
    def last_block(self):
        return self.chain[-1]

    def new_data(self,data_val):
        datastring={
            "data":data_val
        }
        self.data.append(datastring)
        return self.last_block['index'] + 1

    def hash(self,block):
        string = json.dumps(block,sort_keys=True)

        hex=hashlib.sha256(string.encode()).hexdigest()
        return hex 

blockdata = Blockchain()
blockdata.new_data("data line 1")
blockdata.new_data("data line 2")
blockdata.new_data("data line 3")
blockdata.new_data("data line 4")

blockdata.new_block(100)

blockdata.new_data("data line 5")
blockdata.new_data("data line 6")
blockdata.new_data("data line 7")
blockdata.new_data("data line 8")

blockdata.new_block(100)
print (blockdata.chain)

# Pritish code

# import hashlib
# import random

# class Block:
#     def __init__(self,data):
#         self.data = str(data)
#         self.nonce = random.randint(10000,99999)
#         self.hash = None
#         self.hash = hashlib.sha256((self.data + str(self.nonce)).encode())
#         self.hash = self.hash.hexdigest()
#         print("Block Data:{}".format(self.data))
#         print("Block Hashcode:{}".format(self.hash))
#         print("Block Nonce:{}".format(self.nonce))
#         print("\n")
# def getHash(self):
#         hash = hashlib.sha256((self.data + str(self.nonce)).encode())
#         hash = hash.hexdigest()
#         return hash

#     def getNonce(self):
#         return self.nonce

# B1 = Block("A")
# B2 = Block("mumbai")
# B3 = Block(10000)