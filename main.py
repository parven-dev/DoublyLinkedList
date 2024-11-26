
class Node:
    def __init__(self, value):
        self.value =  value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def append(self, value):
        new_node = Node(value)
        temp = self.head
        if temp is None:
            self.head = new_node
            self.tail = new_node
            self.length +=1
            
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            
            
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        
        self.length -= 1

        print("poped item", temp.value)
        
        
        
        
    
            
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
            


d1 = DoublyLinkedList(4)
d1.append(49)
d1.append(50)
d1.append(509)

d1.pop()
d1.display()
