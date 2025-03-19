from diary.diaryservice import Diary
from diary.diaryservice import Exception
from diary.diaryservice.Exception import DiaryNotFound


class Diaries:
    def __init__(self):
        self.diaries = []

    def get_diaries(self):
        return self.diaries

    def size(self):
        return len(self.diaries)

    def add(self, username, password,id):
        new_diary = Diary(username, password,id)
        self.diaries.append(new_diary)

    def find_by_title(self, password,title):
        for diary in self.diaries:
            if diary.get_password() == password and diary.get_title() == title:
                return diary
        raise DiaryNotFound(f"Diary is unavailable")

    def delete(self, title, password):
        delete_diary = None
        for diary in self.diaries:
            if diary.get_password() == password and diary.get_title() == title:
                 self.diaries.remove(delete_diary)
            else:
                raise DiaryNotFound(f"Diary is unavailable ")
       

    