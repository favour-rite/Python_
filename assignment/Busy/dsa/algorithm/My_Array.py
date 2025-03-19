class MyArray:
    def __init__(self, capacity=0):
        
        self.capacity = capacity
        self.array = []
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def add(self, value):
        if not self.is_full():
            self.array.append(value)
            self.size += 1
        else:
            raise ValueError("Array is full")

    def remove(self, value):
        if value in self.array:
            self.array.remove(value)
            self.size -= 1
        else:
            raise ValueError(f"{value} not found in array")

    def contains(self, value):
        return value in self.array

    def pop(self):
        if not self.is_empty():
            value = self.array.pop()
            self.size -= 1
            return value
        else:
            raise ValueError("Array is empty")

    