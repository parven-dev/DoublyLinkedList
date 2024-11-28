class Node:
    def __init__(self, value) :
        self.value = value
        self.next = None
        self.prev = None
        

class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def swap(self):
        temp = self.head
        tail = self.tail
        
        

        
        
    def display(self):
        temp = self.head
        tail = self.tail 
        print("head", temp.value , "tail=", tail.value)
        print(self.length,"its a length")
        while temp is not None:
            print(temp.value)
            temp = temp.next



d1 = DLinkedList()
d1.append(2)
d1.append(4)
d1.append(5)
d1.append(6)

print(d1.display())