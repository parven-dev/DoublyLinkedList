
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

    
            
    def display(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
            


d1 = DoublyLinkedList(4)
d1.display()
