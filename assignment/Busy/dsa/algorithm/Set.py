class Set:
    def __init__(self):
        self.elements = []
        
    def is_empty(self):
        return len(self.elements) == 0
    
    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)
    
    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
    
    def contains(self, element):
        return element in self.elements
    
    def sorted(self):
        return sorted(self.elements)
    
    
    
