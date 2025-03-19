import unittest
from algorithm import my_stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = my_stack()

    def test_stack_is_empty(self):
        self.assertTrue(self.my_stack.is_empty())

    def test_that_stack_is_full(self):
        for count in range(10):
            self.stack.add(count)
        self.assertTrue(self.stack.is_full(),"Checking if the stack is full ")

    def test_that_an_element_can_be_added(self):
        self.stack.add(1)
        self.stack.add(1)
        self.assertEqual(self.stack.size, 2)
        self.assertEqual(self.stack.stack, [2],"Checking if the an element can be added")

    