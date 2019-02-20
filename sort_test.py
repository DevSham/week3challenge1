#carrying out a unittest on the sort function
import unittest
from sorting import sort
class sortTestCase(unittest.TestCase):
    def test_sorting(self):
        result = sort([1, 9, 9.0, 4.6,5,7,6,10,12,20,30,14,17,12,"d", "u", "g"])
        self.assertEqual(result, {'even': [6, 10, 12, 12, 14, 20, 30], 'odd': [1, 4.6, 5, 7, 9, 9.0, 17], 'char': ['d', 'g', 'u']})