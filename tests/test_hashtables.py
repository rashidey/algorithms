from algorithms.hashtables import *
import unittest

class TestSuite(unittest.TestCase):
    def test_twoSum(self):
        self.assertEqual([0, 1], twoSum([2,7,11,15], 9))
        self.assertEqual([0, 2], twoSum([2,7,11,15], 13))
        self.assertEqual([0, 3], twoSum([2,7,11,15], 17))
        self.assertEqual([0, 1], twoSum([2,7], 9))
        self.assertEqual([0, 1], twoSum([11,15], 26))
        self.assertEqual([1, 2], twoSum([12, 54,1,5,2,7,11,15], 55))
        self.assertEqual([3, 4], twoSum([2,7,11,3,65,15], 68))

if __name__ == '__main__':
    unittest.main()

