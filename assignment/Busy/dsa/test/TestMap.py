import unittest

class TestMap(unittest.TestCase):

    def setUp(self):
        self.my_map = Map()
        
    def test_is_empty(self):
        self.assertTrue(self.my_map.is_empty())
        self.my_map.add("key", "value")
        self.assertFalse(self.my_map.is_empty())
        
    def test_that_element_can_be_add(self):
        self.my_map.add("key1", "value1")
        self.my_map.add("key2", "value2")
        self.assertEqual(self.my_map.get("key1"))
        self.assertEqual(self.my_map.get("key2"))
        
    def test_that_element_can_be_remove(self):
        self.my_map.add("key", "value")
        self.my_map.remove("key")
        with self.assertRaises(KeyError):
            self.my_map.get("key")
        
    def test_that_element_can_be_get(self):
        self.my_map.add("key", "value")
        self.assertEqual(self.my_map.get("key"))
        with self.assertRaises(KeyError):
            self.my_map.get("non existing_key")
        
    def test_that_element_can_be_contains(self):
        self.my_map.add("key", "value")
        self.assertTrue(self.my_map.contains("key"))
        self.assertFalse(self.my_map.contains("non existing_key"))
        
    def test_keys(self):
        self.my_map.add("key1", "value1")
        self.my_map.add("key2", "value2")
        self.assertEqual(set(self.my_map.keys()), {"key1", "key2"})
        
    def test_values(self):
        self.my_map.add("key1", "value1")
        self.my_map.add("key2", "value2")
        self.assertEqual(set(self.my_map.values()), {"value1", "value2"})
        
    def test_size_of_the_map(self):
        self.assertEqual(self.my_map.size(), 0)
        self.my_map.add("key1", "value1")
        self.assertEqual(self.my_map.size(), 1)
        
    def test_that_element_can_be_clear(self):
        self.my_map.add("key1", "value1")
        self.my_map.add("key2", "value2")
        self.my_map.clear()
        self.assertTrue(self.my_map.is_empty())
        
if __name__ == "__main__":
    unittest.main()
