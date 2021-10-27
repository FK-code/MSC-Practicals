class smartcontract():
    def __init__(self,newMessage):
        self.message=newMessage

    def setMessage(self,newMessage):
        self.message=newMessage

    def getMessage(self):
        return self.message

    
sm=smartcontract("smart contract")
newMessage="new contract"
text=sm.getMessage()
print(text)
sm.setMessage(newMessage)
text=sm.getMessage()
print(text)