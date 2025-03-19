class Queue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def enqueue(self, element):
        self.elements.append(element)
    
    def dequeue(self):
        if not self.is_empty():
            return self.elements.pop(0)
        raise ValueError("Queue is empty. Cannot dequeue.")
    
    def peek(self):
        if not self.is_empty():
            return self.elements[0]
        raise ValueError("Queue is empty. No front element.")
    
    def size(self):
        return len(self.elements)
    
    def clear(self):
        self.elements = []
        
   


    

