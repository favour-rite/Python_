import unittest
from unittest import TestCase
from tictactoe import *

from tictactoe.Board import Board


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_board_exist(self):
        self.assertEqual()


if __name__ == '__main__':
    unittest.main()
