from autocomplete import Trie

# Initialize the Trie
trie = Trie()

# Load words from example_words.txt
with open('examples/example_words.txt', 'r') as file:
    for line in file:
        word = line.strip()
        trie.insert(word)

# Test autocomplete with a prefix
prefix = "he"
suggestions = trie.autocomplete(prefix)
print(f"Autocomplete suggestions for '{prefix}': {suggestions}")

# Insert the word "hello" multiple times to increase its frequency
trie.insert("hello")
trie.insert("hello")
trie.insert("hero")

# Test autocomplete again to see frequency-based ranking
suggestions = trie.autocomplete(prefix)
print(f"Autocomplete suggestions for '{prefix}' after adding more 'hello' and 'hero': {suggestions}")

