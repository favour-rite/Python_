from datetime import datetime

class User:

    @staticmethod
    def main_menu():
        print("""
                    Welcome to Skye Diary......
            *** Customer Satisfaction, Our Priority ***
                ++++ Safe Secret Deserves A Safe App ++++
            
            1. -> Create New Entry.
            2. -> View Entry.
            3. -> Update Entry.
            4. -> Delete Entry.
            5. -> Lock Diary.
            6. -> Unlock Diary.
            7. -> Help.
            8. -> Exit.
            """)
        User.users_choice()

    @staticmethod
    def users_choice():
        choice = int(input("Input Your Choice: "))
        if choice == 1:
            User.create_new_entry()
        elif choice == 2:
            User.view_entry()
        elif choice == 3:
            User.update_entry()
        elif choice == 4:
            User.delete_entry()
        elif choice == 5:
            User.lock_diary()
        elif choice == 6:
            User.unlock_diary()
        elif choice == 7:
            User.exit()
        else:
            print("Invalid Option. Try again......")
            User.main_menu()

    @staticmethod
    def create_new_entry():
        entry_id = input("Enter entry ID: ")
        title = input("Enter entry title: ")
        content = input("Enter entry content: ")
        date = input("Enter entry date (yyyy-MM-dd HH:mm:ss): ")
       # current_date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        User.diary.create_new_entry(entry_id,title,content)
        print("Entry has been created")
        User.main_menu()

    @staticmethod
    def view_entry():
        entry_id = input("Enter entry ID to view: ")
        User.diary.view_entry(entry_id)
        User.main_menu()

    @staticmethod
    def update_entry():
        entry_id = input("Input entry ID to update: ")
        content = input("Input new content: ")
        # date = input("Input new date (yyyy-MM-dd HH:mm:ss): ")
        # current_date_time = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        User.diary.update_entry(entry_id, content)
        User.main_menu()

    @staticmethod
    def delete_entry():
        entry_id = input("Enter entry ID to delete: ")
        User.diary.delete_entry(entry_id)
        User.main_menu()

    @staticmethod
    def lock_diary():
        entry_id = input("Enter entry ID to lock: ")
        print("Locking diary...")
        User.main_menu()

    @staticmethod
    def unlock_diary():
        entry_id = input("Enter entry ID to unlock: ")
        print("Unlocking diary...")
        User.main_menu()

    @staticmethod
    def exit():
        print("Exiting the application... Thanks For Using Skye Diary")
        exit()


if __name__ == "__main__":
    User.main_menu()
