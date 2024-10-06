class Node:
    def _init_(self,value,next=None):
        self.value = value
        self.next = None
        
class LinkedList:
    def _init_(self,head = None):
        self.head = head
        
    def insert_at_end(self,value):
        new_node = Node(value)
        currentnode = self.head
        while currentnode.next:
            currentnode = currentnode.next
        currentnode.next = new_node
    def display(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.value)
            currentnode = currentnode.next
    def display(self):
       currentnode = self.head
        while currentnode:
            print(currentnode.value)
            currentnode = currentnode.next
            
    def traverse(self):
        currentnode = self.head
        while currentnode:
            currentnode = currentnode.next
        return currentnode
    
    def delete_at_end(self):
        currentnode = self.head
        if not currentnode:
            print("Underflow")
            return
        while currentnode.next.next:
            currentnode = currentnode.next
        del currentnode.next
        currentnode.next = None
        
class Stack(LinkedList):
    def _init_(self):
        super()._init_()
        
    def push(self,value):
        insert_at_end(value)
        
    def pop(self):
        delete_at_end()
        
    def peek(self):
        print(traverse()," <-- Top")
        
s = Stack()
s.pop()
