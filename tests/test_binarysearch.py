from algorithms.binarysearch import *
import unittest

class TestSuite(unittest.TestCase):
    def test_search_insert_position(self):
        self.assertEqual(search_insert_position([1,3,5,6], 5), 2)
        self.assertEqual(search_insert_position([1,3,5,6], 2), 1)
        self.assertEqual(search_insert_position([1,3,5,6], 7), 4)
        self.assertEqual(search_insert_position([1,3,5,6], 0), 0)

    def test_square(self):
     	self.assertEqual(valid_square(16), True)
     	self.assertEqual(valid_square(14), False)































































