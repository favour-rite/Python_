class EntryNotFound(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
class DiaryIsLocked(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class EntryWithTheGivenPassword(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class EntryWithTheGivenId(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
class DiaryNotFound(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)