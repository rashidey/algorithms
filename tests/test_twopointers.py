from algorithms.twopointers import *
import unittest

class TestSuite(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([0,0,1,1,1,2,2,3,3,4]), 5)
        self.assertEqual(remove_duplicates([1,1,2]), 2)

    def test_remove_element(self):
        self.assertEqual(remove_element([3,2,2,3], 3), 2)
        self.assertEqual(remove_element([0,1,2,2,3,0,4,2], 2), 5)
    