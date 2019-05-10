from algorithms.trie import *
import unittest

class TestTrie(unittest.TestCase):
    def test_trie_implementation(self):
        words = Trie()
        words.insert('apple')
        self.assertEqual(words.search('apple'), True)
        self.assertEqual(words.search('app'), False)

    def test_replace_words(self):
        words = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        output = "the cat was rat by the bat"
        #self.assertEqual(replace_words(words, sentence), output)
        
        words = ["a", "aa", "aaa", "aaaa"]
        sentence = "a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"
        output = "a a a a a a a a bbb baba a"
        self.assertEqual(replace_words(words, sentence), output)

    def test_longest_word_dictionary(self):
        words = ["w","wo","wor","worl", "world"]
        self.assertEqual(longest_word(words), 'world')