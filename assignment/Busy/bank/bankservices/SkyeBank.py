import Bank
class SkyeBank:
    
    skye_bank = Bank.Bank()

    @staticmethod
    def main_menu():
        print("""
                        Welcome to Skye Bank......
                *** Customer Satisfaction, Our Priority ***

                1. -> Create Account.
                2. -> Deposit .
                3. -> Withdraw.
                4. -> Transfer.
                5. -> Check Balance.
                6. -> Help.
                7. ->  Call Customer Care...
                8. -> Exit..
                """)
        #choice = int(input("Input Your Choice: "))
        SkyeBank.users_choice()

    @staticmethod
    def users_choice():
        choice = int(input("Input Your Choice: "))
        if choice == 1:
            SkyeBank.create_account()
        elif choice == 2:
            SkyeBank.deposit()
        elif choice == 3:
            SkyeBank.withdraw()
        elif choice == 4:
            SkyeBank.transfer()
        elif choice == 5:
            SkyeBank.check_balance()
        elif choice == 6:
            SkyeBank.help()
        elif choice == 7:
            SkyeBank.call_customer_care()
        elif choice == 8:
            SkyeBank.exit()
        else:
            print("Invalid Option, Try again...")
            SkyeBank.main_menu()

    @staticmethod
    def create_account():
        first_name = input("Input First Name: ")
        last_name = input("Input Last Name: ")
        phone_number = input("Input Phone Number: ")
        password = int(input("Input Password: "))

        account = SkyeBank.skye_bank.create_account(first_name, last_name, password, phone_number)
        print("Account created successfully!!!")
        print(f"Your account number is {account.account_number}")
        SkyeBank.main_menu()

    @staticmethod
    def deposit():
        account_number = int(input("Input Account Number: "))
        amount = float(input("Input amount to deposit: "))
        password = int(input("Input Password: "))

        if SkyeBank.skye_bank.deposit(amount, account_number, password):
            print("Deposit successful!!")
            print(f"You have deposited {amount}")
        else:
            print("Invalid account or password!")
        SkyeBank.main_menu()

    @staticmethod
    def withdraw():
        account_number = int(input("Input Account Number: "))
        withdraw_amount = float(input("Input amount to withdraw: "))
        password = int(input("Input Password: "))

        if SkyeBank.skye_bank.withdraw(withdraw_amount, password, account_number):
            print("Amount has been withdrawn successfully.")
            account = SkyeBank.skye_bank.accounts[account_number]
            print(f"You have withdrawn {withdraw_amount}. Your account balance is {account.get_balance()}")
        else:
            print("Insufficient funds or invalid account/password.")
        SkyeBank.main_menu()

    @staticmethod
    def transfer():
        sender_account = int(input("Input sender's account number: "))
        receiver_account = int(input("Input receiver's account number: "))
        amount = float(input("Input amount to transfer: "))
        password = int(input("Input your password: "))

        sender = SkyeBank.skye_bank.accounts.get(sender_account)
        receiver = SkyeBank.skye_bank.accounts.get(receiver_account)

        if sender and receiver and sender.password == password and sender.account_number:
            if sender.withdraw(amount):
                receiver.deposit(amount)
                print(f"Your transaction of {amount} has been transferred successfully.")
                print(f"Your balance is {sender.get_balance()}")
            else:
                print("Insufficient funds for transfer.")
        else:
            print("Invalid sender account or password.")
        SkyeBank.main_menu()

    @staticmethod
    def check_balance():
        account_number = int(input("Input account number: "))
        password = int(input("Input your password: "))

        balance = SkyeBank.skye_bank.check_balance(account_number, password)
        if balance is not None:
            print(f"Your balance is: {balance}")
        else:
            print("Invalid account number or password.")
        SkyeBank.main_menu()

    @staticmethod
    def help():
        print("""
                Company
                About us
                Press & Media
                Contact us
                Report an Issue
                Security
                Resources
                Privacy Policy
                Terms & Conditions
                Documentation
                Personal
                Business
                """)
        print("For MORE DETAILS VISIT THE HEADQUARTER OF SKYE BANK PLC")
        SkyeBank.main_menu()

    @staticmethod
    def call_customer_care():
        print("Dialing... Network Failed, Please try again...")
        SkyeBank.main_menu()

    @staticmethod
    def exit():
        print("Thanks for Your Patronage!!!")
        print("We are here for you to provide quick customer service.")
        print("Visit our in-app customer service center or physical customer service center or send us a message via official social media or call us via hotline: ** Dial 777 **")
        exit()


if __name__ == "__main__":
    SkyeBank.main_menu()
