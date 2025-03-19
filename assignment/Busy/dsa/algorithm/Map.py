class Map:
    def __init__(self):
        self.elements = {}
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def add(self, key, value):
        self.elements[key] = value
    
    def remove(self, key):
        if key in self.elements:
            del self.elements[key]
        else:
            raise KeyError("Key not found.")
    
    def get(self, key):
        if key in self.elements:
            return self.elements[key]
        else:
            raise KeyError("Key not found.")
    
    def contains(self, key):
        return key in self.elements
    
    def keys(self):
        return list(self.elements.keys())
    
    def values(self):
        return list(self.elements.values())
    
    def size(self):
        return len(self.elements)
    
    def clear(self):
        self.elements = {}

        
    
