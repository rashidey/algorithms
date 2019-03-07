from algorithms.hashtables import *
import unittest

class TestSuite(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual([0, 1], two_sum([2,7,11,15], 9))
        self.assertEqual([0, 2], two_sum([2,7,11,15], 13))
        self.assertEqual([0, 3], two_sum([2,7,11,15], 17))
        self.assertEqual([0, 1], two_sum([2,7], 9))
        self.assertEqual([0, 1], two_sum([11,15], 26))
        self.assertEqual([1, 2], two_sum([12, 54,1,5,2,7,11,15], 55))
        self.assertEqual([3, 4], two_sum([2,7,11,3,65,15], 68))

    def test_three_sum(self):
        self.assertEqual(three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2], [-1,0,1]])
        self.assertEqual(three_sum([-2,0,1,1,2]), [[-2, 0, 2], [-2, 1, 1]])
        self.assertEqual(three_sum([0,0,0,0]), [[0,0,0]])
if __name__ == '__main__':
    unittest.main()

