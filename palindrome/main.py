class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DDl:
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
        self.length +=1
    
    def plindrome(self):
        pass
        
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            
        
d1 = DDl()
d1.append(3)
d1.append(4)
d1.append(5)
d1.append(4)
d1.append(3)
d1.display()
