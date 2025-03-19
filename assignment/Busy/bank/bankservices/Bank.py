from bank.bankservices.Account import Account


class Bank:
    def __init__(self):

        self.accounts = {}


    def create_account(self, first_name, last_name, password,phone_number,account_number):
         account = Account(first_name, last_name, password, phone_number, account_number)
         self.accounts[account.account_number()] = account

         print("Account Has Been Created\n")
         print("Account number: " + account.get_account_number())







    # def deposit(self, amount, account_number, password):
    #     account = self.accounts.get(account_number)
    #     if account_number == account._account_number and account.password == password:
    #         account.deposit(amount)
    #         return account.get_balance()
    #     return None
    #
    # def withdraw(self, amount, password, account_number):
    #     account = self.accounts.get(account_number)
    #     if account.password == password and account.account_number == account_number:
    #         account.withdraw(amount)
    #         return account.get_balance()
    #     return None
    #
    # def check_balance(self, account_number, password):

    # def transfer(self,reciever_account,sender_account,account_number,password):
    #     account = self.accounts.get(account_number)
    #     if account.account_number == sender_account and account.password == password:
    #         amount = account.get_balance()
    #         account.withdraw(amount)
    #         receiver = self.accounts.get(reciever_account)
    #         receiver.transfer(amount)
    #     return receiver.get_balance()
    #
    #     account1 = reciever_account(account_number,password)
    #     account2 = sender_account(account_number,password)
    #
    #
    #
    # def validatePhone_number(self, __phone_number):
    #     if (__phone_number is None
    #                 or __phone_number == ""
    #                 or len(__phone_number) < 11
    #                 or __phone_number.isalpha()):
    #             raise ValueError("Phone number is not valid")
    #
    #
    #
    def check_balance(self, account_number, password):
        account = self.accounts.get(account_number)
        if account.password == password and account.account_number == account_number:
            return account.get_balance()
        return None
