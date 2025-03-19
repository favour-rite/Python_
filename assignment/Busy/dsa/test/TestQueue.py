import unittest

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()
        
    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue(1)
        self.assertFalse(self.queue.is_empty())
        
    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size(), 2)
        
    def test_dequeue(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        element = self.queue.dequeue()
        self.assertEqual(element, 1)
        self.assertEqual(self.queue.size(), 1)
        element = self.queue.dequeue()
        self.assertEqual(element, 2)
        self.assertTrue(self.queue.is_empty())
        
    def test_peek(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.peek(), 1)
        self.queue.dequeue()
        self.assertEqual(self.queue.peek(), 2)
        
    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)
        
    def test_clear(self):
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.clear()
        self.assertTrue(self.queue.is_empty())
        
if __name__ == "__main__":
    unittest.main()
