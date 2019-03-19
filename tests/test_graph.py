from algorithms.graphs import *
import unittest

class TestSuite(unittest.TestCase):
	def test_word_ladder(self):
		self.assertEqual(word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']), 0)
		self.assertEqual(word_ladder('hit', 'cog', ["hot","dot","dog","lot","log","cog"]), 5)