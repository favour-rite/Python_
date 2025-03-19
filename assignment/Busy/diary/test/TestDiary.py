import unittest

from diary.diaryservice import Entry
from diary.diaryservice.Diary import Diary

class TestDiary(unittest.TestCase):

    def setUp(self):
        self.diary = Diary(1234, "username", "PASSWORD")

    def test_initial_state(self):
        self.assertTrue(self.diary.get_is_on,False)
    def test_that_diary_is_un_locked(self):
        self.diary.un_locked()
        self.assertTrue(self.diary.get_is_on,True)

    def test_that_diary_is_locked(self):
        self.diary.is_locked()
        self.assertTrue(self.diary.get_is_on,False)

    def test_that_diary_can_be_created(self):
        self.diary.un_locked()
        self.diary.create_diary(1234,"username","PASSWORD")
        self.assertEqual(self.diary.get_username(), "username")
        self.assertEqual(self.diary.get_password(), "password")
        self.assertEqual(self.diary.get_id(),"id")

    def test_that_entry_can_be_created(self):
        self.diary.un_locked()
        self.diary.create_entry(1234,"content","date","title")
        self.assertEqual(self.diary.size(), 1, "Create new entry")

    def test_that_diary_can_be_unlocked(self):
        self.diary.un_locked()
        self.diary.get_password()
        self.assertTrue(self.diary.un_locked(), "password")

    def test_that_diary_can_be_locked(self):
        self.diary.un_locked()
        self.diary.get_password()
        self.assertTrue(self.diary.un_locked(), "password")

    def test_that_entry_can_be_found_by_id(self):
        self.diary.un_locked()
        self.assertTrue(self.diary.un_locked())
        self.diary.create_entry(1234,"content","date","title")

    def test_update_entry(self):
        self.diary.unlock_diary(self.diary.get_password())
        self.assertTrue(self.diary.un_locked())

        entry = Entry(1, "Content", "2025-02-20", "Title")
        self.diary.entries.append(entry)
        self.diary.update_entry(1, "Updated Content", "2025-02-21")
        self.assertEqual(entry.get_content(), "Updated Content")

        
    ## def test_find_entry_by_id(self):
    #     self.diary.unlock_diary(self.diary.get_password(),)
    #     self.assertTrue(self.diary.unlocked)
    #
    #     entry = Entry(1, "Content", "2025-02-20", "Title")
    #     self.diary.entries.append(entry)
    #     self.assertEqual(self.diary.find_entry_by_id(1), entry)
    # def test_delete_entry(self):
    #     self.diary.unlock_diary(self.diary.get_password(),)
    #     self.assertTrue(self.diary.unlocked)
    #
    #     entry = Entry(1, "Content", "2025-02-20", "Title")
    #     self.diary.entries.append(entry)
    #     self.diary.delete_entry(1)
    #     self.assertEqual(self.diary.size(), 0)
    #
    # def test_view_entry(self):
    #     self.diary.unlock_diary(self.diary.get_password(),)
    #     self.assertTrue(self.diary.unlocked)
    #     entry = Entry(1, "Content", "2025-02-20", "Title")
    #     self.diary.entries.append(entry)
    #     self.diary.view_entry(1, "password")
    #     self.assertEqual(entry.get_content())

if __name__ == "__main__":
    unittest.main()
