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
	
	
def character(text):
    myList = text.lower().split('.')
    myDict = {}

    for count in range(len(myList)):
        words = myList[count].split()
        for word in words:
            if word not in myDict:
                myDict[word] = [count]
            else:
                if count not in myDict[word]:
                    myDict[word].append(count)

    return myDict
if __name__ == "__main__":
	unittest.main()
