if __name__ == "__main__":
    # Create a new Trie and insert some words
    trie = Trie()
    words = ["hello", "hell", "heaven", "heavy", "hero", "herald", "herb"]
    for word in words:
        trie.insert(word)

    # Test autocomplete
    prefix = "he"
    print(f"Autocomplete suggestions for '{prefix}': {trie.autocomplete(prefix)}")

    # Insert the same word multiple times to simulate higher frequency
    trie.insert("hello")
    trie.insert("hello")
    trie.insert("hero")

    # Test autocomplete again
    print(f"Autocomplete suggestions for '{prefix}' after adding more 'hello' and 'hero': {trie.autocomplete(prefix)}")
