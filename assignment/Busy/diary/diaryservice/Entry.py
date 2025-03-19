
from datetime import date

class Entry:
    def __init__(self, id, content, title):
        self.id = id
        self.content = content
        self.date = date.today()
        self.title = title

    def get_id(self):
        return self.id
    
    def set_content(self, text):
        self.content = text
    def get_content(self):
        return self.content
    
    def set_date(self,date):
        self.date = date
    def get_date(self):
        return self.date
   
    def set_title(self, new_title):
        self.title = new_title
    def get_title(self):
        return self.title

    #def __str__(self):
     #   return f"Entry:\nID: {self.id},\nTitle: {self.title},\n content: {self.content},\n date: {date}
    def __str__(self):
        return f"Entry:\nID: {self.id},\nTitle: {self.title},\nBody: {self.body},\nDateCreated: {self.date_created}"
