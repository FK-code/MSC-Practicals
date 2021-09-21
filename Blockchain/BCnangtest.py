from BCnang import *
from time import time
import pprint

pp = pprint.PrettyPrinter(indent=4)

blockchain=Blockchain()
data=["First block?"]

blockchain.pendingdata.append(data)
# blockchain.minependingData()

pp.pprint(blockchain.chainJSONencode())
print("Lenght : ", len(blockchain.chain))
