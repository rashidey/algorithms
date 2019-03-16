from algorithms.dp import *
import unittest

class TestSuite(unittest.TestCase):
    def test_pascal(self):
        self.assertEqual(pascal(1), [[1]])
        self.assertEqual(pascal(2), [[1], [1,1]])
        self.assertEqual(pascal(3), [[1], [1,1], [1,2,1]])
        self.assertEqual(pascal(4), [[1], [1,1], [1,2,1],[1,3,3,1]])

    def test_pascal(self):
        self.assertEqual(pascal_row(1), [1])
        self.assertEqual(pascal_row(2), [1,1])
        self.assertEqual(pascal_row(3), [1,2,1])
        self.assertEqual(pascal_row(4), [1,3,3,1])
