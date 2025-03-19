import unittest

from bank.bankservices.Account import Account
from bank.bankservices.Bank import Bank
from bank.bankservices.Exception import InvalidAmountException



class BankTest(unittest.TestCase):

    def setUp(self):
        self.bank = Bank()

    def test_bank_is_not_null(self):
        self.assertIsNotNone(self.bank,"bank should be in existence")

    def test_that_account_can_be_created(self):
        first_name = "favy"
        last_name = "rite"
        balance = 0.0
        password = 1234
        account_number = 7777
        self.bank.create_account(first_name, last_name, password, account_number)
        self.assertEqual(self.bank.create_account(),)



        if __name__ == '__main__':
            unittest.main()

