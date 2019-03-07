from algorithms.stack import *
import unittest

class TestSuite(unittest.TestCase):
    def test_isValid(self):
        self.assertEqual(True, isValid('()'))
        self.assertEqual(True, isValid('()[]{}'))
        self.assertEqual(False, isValid('(]'))
        self.assertEqual(False, isValid('([)]'))
        self.assertEqual(True, isValid('{[]}'))

if __name__ == '__main__':
    unittest.main()