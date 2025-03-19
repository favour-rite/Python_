class my_stack:
    def __init__(self,capacity=10):
        self.size = 0
        self.capacity = capacity
        self.top=-1
        self.stack = []
    
    def is_empty(self):
        return self.stack == 0
    
    def is_full(self):
        return self.size == self.capacity

    def add(self,value):
        if not self.is_full():
            self.stack.append(value)
            self.size +=1
        else: raise ValueError("stack is full")

    def pop(self):
        if not self.is_empty():
            self.size -=1
            return self.stack.pop()
        else: raise ValueError("stack is empty")