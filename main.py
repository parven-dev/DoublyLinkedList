
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
        if self.length == 1:
            self.head = None
            self.tail = None
        else:  
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        
        self.length -= 1
        return temp.value, "poped noded"

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length +=1 
        return True
    
    def pop_first(self):
        temp = self.head 
        
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.prev  = None 
            temp.next = None  
        self.length=-1         
        return temp.value, "poped value"
    
    def get(self, index):
        if index <  0 or index  >= self.length:
            return None
        
        temp = self.head
        if self.length /2 > index:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1,index,  -1):
                temp = temp.prev
        
        return temp.value
        
    
          
    def display(self):
        temp = self.head
        while temp.next is not None:
            print(temp.value, end="->")
            temp = temp.next
        
            


d1 = DoublyLinkedList(4)
d1.append(49) 
d1.prepend(55)
d1.prepend(400)



# print(d1.pop())
# print(d1.pop())

# print(d1.pop())
# d1.pop_first()
print(d1.get(1))
print(d1.get(2))
print(d1.get(0))



