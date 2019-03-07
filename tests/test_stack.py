from algorithms.stack import *
import unittest

class TestSuite(unittest.TestCase):
    def test_is_valid(self):
        self.assertEqual(True, is_valid('()'))
        self.assertEqual(True, is_valid('()[]{}'))
        self.assertEqual(False, is_valid('(]'))
        self.assertEqual(False, is_valid('([)]'))
        self.assertEqual(True, is_valid('{[]}'))

if __name__ == '__main__':
    unittest.main()