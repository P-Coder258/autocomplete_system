import unittest
from autocomplete import Trie

class TestTrie(unittest.TestCase):

    def setUp(self):
        """Set up the Trie and add some initial words."""
        self.trie = Trie()
        words = ["hello", "hell", "heaven", "heavy", "hero", "herald", "herb"]
        for word in words:
            self.trie.insert(word)

    def test_insert_and_search(self):
        """Test that words are correctly inserted and can be found."""
        self.assertIsNotNone(self.trie.search("hello"))
        self.assertIsNone(self.trie.search("helix"))  # Word not in the Trie

    def test_autocomplete(self):
        """Test that autocomplete suggestions are correct."""
        suggestions = self.trie.autocomplete("he")
        expected_suggestions = ["hello", "hell", "heaven", "heavy", "hero", "herald", "herb"]
        self.assertEqual(sorted(suggestions), sorted(expected_suggestions))

    def test_autocomplete_with_frequency(self):
        """Test that autocomplete suggestions are sorted by frequency."""
        # Insert the word "hello" multiple times to increase its frequency
        self.trie.insert("hello")
        self.trie.insert("hello")
        self.trie.insert("hello")
        self.trie.insert("hero")

        suggestions = self.trie.autocomplete("he")
        self.assertEqual(suggestions[0], "hello")
        self.assertEqual(suggestions[1], "hero")

    def test_empty_prefix(self):
        """Test autocomplete with an empty prefix (should return no suggestions)."""
        suggestions = self.trie.autocomplete("")
        self.assertEqual(suggestions, [])

    def test_no_matching_prefix(self):
        """Test autocomplete with a prefix that has no matches."""
        suggestions = self.trie.autocomplete("xyz")
        self.assertEqual(suggestions, [])

if __name__ == "__main__":
    unittest.main()
