from typing import Dict, List, Optional

class TrieNode:
    """Node class for Trie"""
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.word_count: int = 0

class Trie:
    """Trie (Prefix Tree) implementation"""
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie
        
        Args:
            word: Word to be inserted
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += 1
        node.is_end_of_word = True
    
    def search(self, word: str) -> bool:
        """
        Search for a word in the trie
        
        Args:
            word: Word to search for
            
        Returns:
            True if word exists in trie, False otherwise
        """
        node = self._get_node(word)
        return node is not None and node.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in the trie starts with the given prefix
        
        Args:
            prefix: Prefix to check
            
        Returns:
            True if prefix exists in trie, False otherwise
        """
        return self._get_node(prefix) is not None
    
    def count_words_with_prefix(self, prefix: str) -> int:
        """
        Count the number of words that start with the given prefix
        
        Args:
            prefix: Prefix to count words for
            
        Returns:
            Number of words starting with the prefix
        """
        node = self._get_node(prefix)
        return node.word_count if node else 0
    
    def delete(self, word: str) -> bool:
        """
        Delete a word from the trie
        
        Args:
            word: Word to delete
            
        Returns:
            True if word was deleted, False if word doesn't exist
        """
        if not self.search(word):
            return False
            
        node = self.root
        stack = []
        
        # Find the path to the word
        for char in word:
            stack.append((node, char))
            node = node.children[char]
            node.word_count -= 1
        
        # Mark as not end of word
        node.is_end_of_word = False
        
        # Remove nodes if they have no children and are not end of word
        while stack and not node.children and not node.is_end_of_word:
            parent, char = stack.pop()
            del parent.children[char]
            node = parent
        
        return True
    
    def get_all_words(self) -> List[str]:
        """
        Get all words stored in the trie
        
        Returns:
            List of all words in the trie
        """
        words = []
        
        def _get_words(node: TrieNode, prefix: str) -> None:
            if node.is_end_of_word:
                words.append(prefix)
            
            for char, child in node.children.items():
                _get_words(child, prefix + char)
        
        _get_words(self.root, "")
        return words
    
    def _get_node(self, prefix: str) -> Optional[TrieNode]:
        """
        Get the node corresponding to the last character of the prefix
        
        Args:
            prefix: Prefix to find node for
            
        Returns:
            Node if prefix exists, None otherwise
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

# Example usage
if __name__ == "__main__":
    # Create a trie
    trie = Trie()
    
    # Insert words
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")
    
    # Test search
    search_words = ["apple", "app", "ban", "orange"]
    print("\nSearch results:")
    for word in search_words:
        print(f"Searching for '{word}': {trie.search(word)}")
    
    # Test prefix
    prefixes = ["app", "ban", "ora"]
    print("\nPrefix results:")
    for prefix in prefixes:
        print(f"Starts with '{prefix}': {trie.starts_with(prefix)}")
        print(f"Words with prefix '{prefix}': {trie.count_words_with_prefix(prefix)}")
    
    # Test get all words
    print("\nAll words in trie:")
    print(trie.get_all_words())
    
    # Test deletion
    delete_words = ["app", "banana", "orange"]
    print("\nDeletion results:")
    for word in delete_words:
        result = trie.delete(word)
        print(f"Deleted '{word}': {result}")
        print(f"All words after deletion: {trie.get_all_words()}") 