class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None

noNodes = "No nods in the list "
class linkedlist:
    def __init__(self):
        self.head = None
    
    def append(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.nextNode:
            current = current.nextNode
        current.nextNode = node
        print("node was added to the list")

    def insert(self,data):
        node = Node(data)
        if not self.head:
            self.head = node
            return
        
        node.nextNode = self.head
        self.head = node
        print("node was inserted successfully")
        
    def display(self):
        if not self.head:
            print(noNodes)
            return
        current = self.head
        while current:
            print(current.data,end=" -> ")
            current = current.nextNode
        print("None")

    def delete(self,value):
        if not self.head:
            print(noNodes)   
            return
        
        if self.head.data == value:
            self.head = self.head.nextNode
            print("node was deleted ")
            return
        
        current = self.head
        prev_node = None
        while current:
            if current.data == value:
                prev_node.nextNode = current.nextNode
                print("node was deleted")
                return
            prev_node = current
            current = current.nextNode

    def search(self,value):
        if not self.head:
            print(noNodes)
            return
        
        current = self.head
        while current:
            if current.data == value:
                print(f"value {value} was found in the list")
                return
            current = current.nextNode
        print("Sorry value wasn't found")

    def count_nodes(self):
        if not self.head:
            print(noNodes)
            return
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.nextNode
        
        return count

    def insert_by_index(self,data,index):
        newNode = Node(data)

        if index < 0 :
            return print("invalid index")

        if index == 0:
            newNode.nextNode = self.head
            self.head = newNode
            return

        current = self.head
        count = 0

        while current and count < index -1:
            current = current.nextNode
            count += 1
        
        if count != index:
            return print("invalid index")
        newNode.nextNode = current.nextNode
        current.nextNode = newNode
    
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_node = curr.nextNode
            curr.nextNode = prev
            prev = curr
            curr = next_node

        self.head = prev
       
    def is_empty(self):
        return not self.head
    
    def clear(self):
        self.head = None

    def to_list(self):
        listofNodes = []
        current = self.head
        while current:
            listofNodes.append(current.data)
            current = current.nextNode
        
        return listofNodes
        
    def from_list(self,list):
        self.head = None
        for data in list:
            self.append(data)
            

      
L = linkedlist()
L.from_list([10,20,30,40,50,60,70])
L.display()
print(L.to_list())



