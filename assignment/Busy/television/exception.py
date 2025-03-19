class VolumeIsLowException(Exception):
    def __init__(self,message):
        self.message = message
        super("Volume is out of range").__init__(self.message)
class VolumeIsHighException(Exception):
    def __init__(self,message):
        self.message = message
        super("Volume is out of bound").__init__(self.message)        
    
class ChannelIsIncreasedException(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class ChannelIsDecreasedException(Exception):
    def __init__(self,message):
        self.message = message
        super("Television Channel is out of bound").__init__(self.message)

class TelevisionIsMutedException(Exception):
    def __init__(self,message):
        self.message = message
        super("Television volume is muted").__init__(self.message)

class TelevisionIsUnmutedException(Exception):
    def __init__(self,message):
        self.message = message
        super("Television volume is un muted").__init__(self.message)