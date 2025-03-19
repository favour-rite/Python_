import unittest
import get_suum_even


class test_sum_even(unittest.TestCase):

	

	def test_that_get_suum_even_returns(self):
		number = [1,2,3,4,5]
		actual = get_suum_even.get_suum_even(number)
		expected = 6
		self.assertEqual(actual, expected)
	
	def test_that_get_suum_even_returns(self):
		number = [1,2,3,4,5]
		actual = get_suum_even.get_suum_even(number)
		expected = 
		self.assertEqual(actual, expected)
	
	

if __name__ == "__main__":
	unittest.main()
