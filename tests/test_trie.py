from algorithms.trie import *
import unittest

class TestTrie(unittest.TestCase):
    def test_trie_implementation(self):
        words = Trie()
        words.insert('apple')
        self.assertEqual(words.search('apple'), True)
        self.assertEqual(words.search('app'), False)
