from algorithms.bits import *
import unittest

class TestSuite(unittest.TestCase):
	def test_single_number(self):
		self.assertEqual(single_number([1,1,2,2,3]), 3)