import unittest

from bank.bankservices.Account import Account
from bank.bankservices.Exception import InvalidAmountException


class AccountTest(unittest.TestCase):

    def setUp(self):
        self.account = Account("first_name","last_name", 1234,  0000)


    def test_account_number_is_zero_by_default(self):
        self.assertEqual(0.0,self.account.get_balance())

    def test_that_account_is_not_null(self):
        self.assertIsNotNone(self.account, "account should not be null")

    def test_that_money_can_be_deposited_into_my_account(self):
        self.account.deposit(200)
        self.account.deposit(200)
        self.assertEqual(400.00, self.account.get_balance(), " Current deposit is 400.00 ")

    def test_that_money_deposited_is_not_a_negative_number(self):
        self.assertRaises(InvalidAmountException, self.account.deposit, -200)


    def test_that_money_can_be_withdraw_from_user(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        self.assertEqual(300,self.account.get_balance()," Money should be 300,after withdraw ")

    def test_that_money_withdrawn_is_not_a_negative_number(self):
        self.assertRaises(InvalidAmountException, self.account.withdraw, -400)



    # def test_that_password_can_be_updated(self):
    #     self.account.update_password("<PASSWORD>")
    #     self.assertEqual(0000,self.account.password(), " Current password is 0000")