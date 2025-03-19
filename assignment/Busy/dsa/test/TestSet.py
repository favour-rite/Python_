import unittest

class TestSet(unittest.TestCase):

    def setUp(self):
        self.my_set = Set()
        
    def test_is_empty(self):
        self.assertTrue(self.my_set.is_empty())
        self.my_set.add(1)
        self.assertFalse(self.my_set.is_empty())
        
    def test_add(self):
        self.my_set.add(1)
        self.my_set.add(1)  
        self.assertEqual(len(self.my_set.elements), 1)
        self.my_set.add(2)
        self.assertEqual(len(self.my_set.elements), 2)
        
    def test_remove(self):
        self.my_set.add(1)
        self.my_set.remove(1)
        self.assertFalse(self.my_set.contains(1))
        self.my_set.remove(2)  
        self.assertEqual(len(self.my_set.elements), 0)
        
    def test_contains(self):
        self.my_set.add(1)
        self.assertTrue(self.my_set.contains(1))
        self.assertFalse(self.my_set.contains(2))
        
    def test_sorted(self):
        self.my_set.add(3)
        self.my_set.add(1)
        self.my_set.add(2)
        self.assertEqual(self.my_set.sorted(), [1, 2, 3])
        
    def test_index(self):
        self.my_set.add(1)
        self.my_set.add(2)
        self.assertEqual(self.my_set.index(1), 0)
        self.assertEqual(self.my_set.index(2), 1)
        self.assertEqual(self.my_set.index(3), -1)
        
    def test_clear(self):
        self.my_set.add(1)
        self.my_set.add(2)
        self.my_set.clear()
        self.assertTrue(self.my_set.is_empty())
        
if __name__ == "__main__":
    unittest.main()
