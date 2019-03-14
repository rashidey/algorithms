from algorithms.math import *
import unittest

class TestSuite(unittest.TestCase):
    def test_add_binary(self):
        self.assertEqual(add_binary('11', '1'), '100')
        self.assertEqual(add_binary('1010', '1011'), '10101')
        self.assertEqual(add_binary('0', '0'), '0')
        self.assertEqual(add_binary('011', '1'), '100')
        self.assertEqual(add_binary('101', '1'), '110')