class Node:
    def __init__(self,nodeName):
        self.nodeName = nodeName
        self.nextNode=None



class LinkedList:
    def __init__(self,rootNode = None):
        self.rootNode = rootNode
        self.lastNode = None

    def addNode(self,Node):
        if self.rootNode is None:
            self.rootNode = Node
            self.lastNode = Node
        else:
            self.lastNode.nextNode = Node
            self.lastNode = Node

    def deleteNode(self,delNode):
        currNode = self.rootNode
        if currNode.nodeName == delNode.nodeName:
            self.rootNode = currNode.nextNode
            return
        while currNode.nextNode.nodeName != delNode.nodeName:
            currNode = currNode.nextNode
        currNode.nextNode = currNode.nextNode.nextNode

        
                
            
    def printNodes(self):
        currNode = self.rootNode
        while currNode is not None:
            print(currNode.nodeName)
            currNode = currNode.nextNode

    


LL = LinkedList()
LL.addNode(Node("A"))
LL.addNode(Node("B"))
LL.addNode(Node("C"))
LL.addNode(Node("D"))
LL.addNode(Node("E"))
LL.printNodes()

print("After deletion")
LL.deleteNode(Node("C"))
LL.printNodes()





