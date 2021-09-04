class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def append(self, data):  # append
        if self.head is None:       # if list is empty
            new_node = Node(data)  # create new node
            new_node.prev = None  # prev pointer of new node to null
            self.head = new_node  # head pointer of self to new node
        else:
            new_node = Node(data)  # create new node
            cur = self.head  # const cur to store self.head
            while cur.next:  # while next point of cur is not null
                cur = cur.next
            cur.next = new_node  # next node to be new node
            new_node.prev = cur  # prev pointer of new node to cur(last node)
            new_node.next = None  # next pointer of new node to null

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and cur == self.head:
                # if list has one node
                if not cur.next:
                    cur = None
                    self.head = None
                    return
                # if list has 2 nodes and node being delete is 1st node
                else:
                    nextnode = cur.next
                    cur.next = None
                    nextnode.prev = None
                    cur = None
                    self.head = nextnode
                    return
            elif cur.data == key:
                # node somewhere is between
                if cur.next:
                    nxtnode = cur.next
                    prevnode = cur.prev
                    prevnode.next = nxtnode
                    nxtnode.prev = prevnode
                    cur.next = None
                    cur.prev = None
                    cur = None
                    return
                # node at the end
                else:
                    prevnode = cur.prev
                    prevnode.next = None
                    cur.prev = None
                    cur = None
                    return
            cur = cur.next

    def update(self, key, newdata):
        flag=False
        cur = self.head
        while cur:
            if cur.data == key:
                cur.data = newdata
                flag=True
                print("List after Update")
                dll.print_list()
            cur = cur.next
        if flag==False:
            print("Node not found")

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

dll = DLL()
flag=True
while flag==True:
    choice=int(input("1. Add Nodes 2. Delete Node 3. Update Node 4. Exit \t"))
    if choice==1:
        node_list=list(input("Enter nodes: \t").split())
        for i in node_list:
            dll.append(i)
        print("List after Adding nodes")
        dll.print_list()
    if choice==2:
        data=input("Enter node to be deleted \t")
        dll.delete(data)
        print("List after Deleting node")
        dll.print_list()
    if choice==3:
        old,new=input("Enter node and data to update \t").split()
        dll.update(old,new) 
    if choice ==4:
        flag=False















# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.append(4)
# dll.append(5)

# print("The list is")
# dll.print_list()

# dll.delete(3)
# print("List after deleting node '3'")
# dll.print_list()

# dll.update(5,"End of list")
# print("List after updating node '5' ,that is the last node")
# dll.print_list()