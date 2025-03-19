class InvalidPinException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
        
class InvalidAmountException(Exception):
    def __init__(self,message):
        self.message = message 
        super().__init__(self,message)