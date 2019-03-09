from algorithms.arrays import *
import unittest

class TestSuite(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(plus_one([1,2,3]), [1,2,4])
        self.assertEqual(plus_one([4,3,2,1]), [4,3,2,2])
        self.assertEqual(plus_one([9,9,9,9]), [1,0,0,0,0])
        self.assertEqual(plus_one([8,9,9,9]), [9,0,0,0])
        self.assertEqual(plus_one([0]), [1])
        self.assertEqual(plus_one([1, 0]), [1, 1])

        
        