import unittest
from myarray import MyArray

class TestMyArray(unittest.TestCase):
    
    def setUp(self):
        self.array = MyArray(capacity = 5)
    
    def test_that_array_is_not_null(self):
        self.assertNotNull(self.array)

    def test_is_empty(self):
        self.assertTrue(self.array.is_empty(),"Checking if the array is empty")

    def test_that_array_can_add_element(self):
        self.array.add(1)
        self.assertEqual(self.array.size, 1)
        self.assertEqual(self.array.array, [1],"Checking if the an element can be added")

    def test_if_the_array_is_full(self):
        for count in range(5):
            self.array.add(count)
        self.assertTrue(self.array.is_full(),"Checking if the array is full")

    def test_that_array_contains_element(self):
        self.array.add(1)
        self.assertTrue(self.array.contains(1))
        self.assertFalse(self.array.contains(2),"Checking if the array contains an element ")

    def test_that_an_element_can_be_remove(self):
        self.array.add(1)
        self.array.add(2)
        self.array.remove(1)
        self.assertEqual(self.array.size, 1)
        self.assertNotIn(1, self.array.array,"You can remove an element")

    
    
if __name__ == '__main__':
    unittest.main()




