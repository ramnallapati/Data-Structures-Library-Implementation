
# test_trie_module.py

import unittest
from ProgrammeFiles.Trie import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        self.trie = Trie()
        self.trie.insert("apple")
        self.trie.insert("app")
        self.trie.insert("application")

    def test_search_existing_word(self):
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertTrue(self.trie.search("application"))

    def test_search_non_existing_word(self):
        self.assertFalse(self.trie.search("apples"))
        self.assertFalse(self.trie.search("banana"))

    def test_starts_with_prefix(self):
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("appl"))
        self.assertFalse(self.trie.starts_with("bana"))

    def test_delete_word(self):
        self.trie.delete("app")
        self.assertFalse(self.trie.search("app"))
        self.assertTrue(self.trie.search("apple"))  # "apple" should remain
        self.assertTrue(self.trie.starts_with("app"))

        self.trie.delete("apple")
        self.assertFalse(self.trie.search("apple"))
        self.assertTrue(self.trie.search("application"))  # "application" should remain

    def test_delete_non_existing_word(self):
        self.assertFalse(self.trie.search("banana"))
        self.trie.delete("banana")  # Should not throw error
        self.assertFalse(self.trie.search("banana"))

if __name__ == '__main__':
    unittest.main()
