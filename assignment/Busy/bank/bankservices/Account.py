
from bank.bankservices.Exception import InvalidPinException, InvalidAmountException

class Account:
    def __init__(self,first_name,last_name,account_number,password):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__account_number = account_number
        self.__password = password
        self.__balance = 0

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name):
        self.__first_name = first_name

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    def get_balance(self):
        return self.__balance

    def password(self):
        return self.__password

    # @self.__password.setter
    # def password(self, __password):
    #     self.__password = __password

    @property
    def account_number(self):
        return self.__account_number


    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise InvalidAmountException("Invalid amount: Be positive for once ")

    def withdraw(self,amount):
        if amount > 0:
            self.__balance -= amount
        else:
            raise InvalidAmountException("Invalid amount: Be positive for once")


    def update_password(self, oldPassword,newPassword):

        if self.__password == oldPassword:
            self.__password = newPassword
        else:
            raise InvalidPinException("Old pin is incorrect")



    def __str__(self):
        return "Account Name: {} {} \nAccount Balance: {} \nAccount Number: {}".format(self.__first_name,self.__last_name, self.__balance,self.__account_number)


















