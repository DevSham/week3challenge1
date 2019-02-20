#carrying out a unittest on the sort function
import unittest
from missing import miss
class missTestCase(unittest.TestCase):
    def test_missing(self):
        result = miss([2,4,5,6,7,8])
        self.assertEqual(result, [0, 1, 3, 9])