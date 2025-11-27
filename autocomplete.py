import time
import logging

# Configure logging to simulate a real production environment
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.frequency = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        # Validate input type to prevent crashes
        if not isinstance(word, str):
            logging.error(f"Insert Failed: Invalid type {type(word)}. Expected string.")
            return False
        
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.is_end_of_word = True
        node.frequency += 1
        # logging.info(f"Inserted: {word}") # Commented out to avoid spamming logs during bulk load
        return True

    def search(self, word):
        if not word: return None
        node = self.root
        for char in word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node if node.is_end_of_word else None

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocomplete(self, prefix):
        """
        Returns a list of suggested words based on prefix, sorted by frequency.
        Includes performance benchmarking.
        """
        start_time = time.time()
        
        try:
            node = self.starts_with(prefix)
            if not node:
                logging.info(f"No results found for prefix: '{prefix}'")
                return []

            words = []
            self._dfs(node, prefix, words)
            
            # Sort by frequency (descending)
            words.sort(key=lambda x: x[1], reverse=True)
            
            results = [word for word, freq in words]
            
            end_time = time.time()
            duration_ms = (end_time - start_time) * 1000
            
            logging.info(f"Search for '{prefix}' returned {len(results)} results in {duration_ms:.4f} ms")
            
            return results
        
        except Exception as e:
            logging.error(f"Error during autocomplete: {e}")
            return []

    def _dfs(self, node, prefix, words):
        if node.is_end_of_word:
            words.append((prefix, node.frequency))
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, words)

# --- DEMONSTRATION BLOCK ---
# This runs when you execute the script, proving it works.

if __name__ == "__main__":
    trie = Trie()
    
    print("--- 1. Loading Data ---")
    # Simulate loading a dictionary
    sample_words = [
        "apple", "app", "application", "apricot", "banana", "band", "bandana", 
        "bat", "batch", "battle", "cat", "caterpillar", "cattle"
    ]
    # Add 'apple' multiple times to test frequency sorting
    sample_words.extend(["apple", "apple", "app", "bat"]) 
    
    for w in sample_words:
        trie.insert(w)
    print(f"Loaded {len(sample_words)} words into the Trie.")

    print("\n--- 2. Benchmarking Search ---")
    # Test 1: Search for 'app'
    results = trie.autocomplete("app")
    print(f"Results for 'app': {results}")

    print("\n--- 3. Testing QA Validation ---")
    # Test 2: Insert invalid data
    trie.insert(12345)  # Should log an error, not crash

    print("\n--- 4. Performance Test ---")
    # Test 3: Search for something that doesn't exist
    trie.autocomplete("zoo")
