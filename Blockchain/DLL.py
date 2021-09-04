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

    def prepend(self, data):  # prepend
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None

    def insert_after_node(self, key, data):
        cur = self.head  # saved head pointer of self in cur
        while cur:
            # if key is last node in list
            if cur.next is None and cur.data == key:
                self.append(data)
                return
            # if key is somewhere in between
            elif cur.data == key:  # node after which to insert // cur node
                new_node = Node(data)  # create new node
                keynode = cur.next  # saved pointer to next node from key to keynode
                cur.next = new_node  # pointer of cur node to new node
                new_node.next = keynode  # pointer to saved next node from key
                new_node.prev = cur  # new node prev pointer points to key
                keynode.prev = new_node  # nxt node prev pointer points to new node
            cur = cur.next

    def insert_before_node(self, key, data):
        cur = self.head
        while cur:
            if cur.prev is None and cur.data == key:
                self.prepend(data)
                return
            elif cur.data == key:
                new_node = Node(data)
                keynode = cur.prev
                keynode.next = new_node
                cur.prev = new_node
                new_node.next = cur
                new_node.prev = keynode
            cur = cur.next

    def delete(self, key):
        cur = self.head

        while cur:
            if cur.data == key and cur == self.head:
                # if list has one node
                if not cur.next:
                    cur = None
                    self.head = None
                    return

                # if list has 2 nodes
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
            cur = cur.next
        if flag==False:
            print("Node not found")

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

dllist = DLL()

# menu=[]

# m=int(input("1. Append \n 2. Prepend \n 3. Delete \n 4. Update \n"))
# if m==1:
#     data=input("enter data you want to append")
#     print (data)
#     (data)
#     # DLL.append(data)
#     # dllist.print_list(input_data)

# if m==2:
#     input_data=input("enter data you want to prepend")
#     DLL.prepend(input_data)
# if m==3:
#     input_data=input("enter data you want to delete")
#     DLL.delete(input_data)
# if m==4:
#     old,new=input("Enter the data you want to update and data to update with").split()
#     DLL.update(old,new)

dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.print_list()
dllist.update(6,67)


dllist.print_list()
