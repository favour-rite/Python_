
from diary.diaryservice import Entry
from diary.diaryservice import Diaries
from diary.diaryservice import Exception
from diary.diaryservice.Exception import EntryNotFound, EntryWithTheGivenId, EntryWithTheGivenPassword, DiaryIsLocked

class Diary:

    def __init__(self, id, username, password):
        self.is_on = False
        self.entries = []
        self.id = id
        self.username = username
        self.password = password

    def get_is_on(self):
        return self.is_on

    def un_locked(self):
        self.is_on = True

    def is_locked(self):
        self.is_on = False

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def get_id(self):
        return self.id

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password

    def set_id(self, id):
        self.id = id

    def size(self):
        return len(self.entries)

    def create_diary(self, id, username, password):
        if self.get_is_on():
            new_diary = Diary(id, username, password)
            self.diaries.add(new_diary)
            print("A new diary has been created.")
        else:
            self.is_locked()
            print("Diary is locked, Cannot create new diary")

    def create_entry(self, id, content, date, title):
        if self.get_is_on():
            new_entry = Entry(id, content, date, title)
            self.entries.append(new_entry)
        else:
            self.is_locked()
            print("Diary is locked, Cannot create new entry")

    def unlock_diary(self, password):
        if self.password == password:
            self.un_locked()
        else:
            raise EntryWithTheGivenPassword("Incorrect credentials")

    def lock_diary(self, password):
        if self.password == password:
            self.is_locked()
        else:
            raise EntryWithTheGivenPassword("Incorrect credentials")




    # def find_entry_by_id(self, id):
    #   if self.un_locked():
    #       for entry in self.entries:
    #           if entry.id == id:
    #             return entry
    #         raise EntryWithTheGivenId("Incorrect Id")
    #
    # def update_entry(self, id, content, date):
    #     if not self.is_locked:
    #         entry = self.find_entry_by_id(id)
    #         if entry is not None:
    #             entry.set_content(content)
    #         else:
    #             raise EntryNotFound("Entry with the given ID not found.")
    #     raise DiaryIsLocked("Diary is locked. Cannot update entry.")
    #
    # def delete_entry(self, id):
    #     if not self.is_locked:
    #         entry = self.find_entry_by_id(id)
    #         if entry is not None:
    #             self.entries.remove(entry)
    #         else: raise EntryNotFound("Entry with the given ID not found.")
    #     raise DiaryIsLocked("Diary is locked. Cannot delete entry.")
    #
    # def view_entry(self, id,password):
    #     for entry in self.entries:
    #         if not self.is_locked:
    #             if self.id == id and self.password == password:
    #                 entry = self.find_entry_by_id(id)
    #         if entry is not None:
    #             print(entry.get_content())
    #         else:
    #             raise EntryNotFound("Entry with the given ID not found.")
    #     raise DiaryIsLocked("Diary is locked. Cannot view")
    #




   






