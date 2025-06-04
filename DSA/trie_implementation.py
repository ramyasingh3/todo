from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class TrieNode:
    """Node class for Trie"""
    children: Dict[str, 'TrieNode']
    is_end_of_word: bool = False
    word_count: int = 0

class Trie:
    """Trie (Prefix Tree) implementation"""
    
    def __init__(self):
        """Initialize Trie with root node"""
        self.root = TrieNode(children={})
    
    def insert(self, word: str) -> None:
        """
        Insert a word into the trie
        
        Args:
            word: Word to insert
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode(children={})
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
    
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words that start with the given prefix
        
        Args:
            prefix: Prefix to search for
            
        Returns:
            List of words starting with the prefix
        """
        node = self._get_node(prefix)
        if node is None:
            return []
        
        words = []
        self._collect_words(node, prefix, words)
        return words
    
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
        while stack and not node.is_end_of_word and not node.children:
            parent, char = stack.pop()
            del parent.children[char]
            node = parent
        
        return True
    
    def get_word_count(self, prefix: str = "") -> int:
        """
        Get count of words with given prefix
        
        Args:
            prefix: Prefix to count words for (empty string for all words)
            
        Returns:
            Number of words with the prefix
        """
        node = self._get_node(prefix)
        return node.word_count if node else 0
    
    def _get_node(self, prefix: str) -> Optional[TrieNode]:
        """
        Get node for given prefix
        
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
    
    def _collect_words(self, node: TrieNode, prefix: str, words: List[str]) -> None:
        """
        Helper method to collect all words from a node
        
        Args:
            node: Current node
            prefix: Current prefix
            words: List to collect words in
        """
        if node.is_end_of_word:
            words.append(prefix)
        
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)

# Example usage
if __name__ == "__main__":
    # Create a trie
    trie = Trie()
    
    # Insert words
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    print("Inserting words:", words)
    for word in words:
        trie.insert(word)
    
    # Test search
    print("\nTesting search:")
    test_words = ["apple", "app", "ban", "banana", "orange"]
    for word in test_words:
        print(f"Search '{word}': {trie.search(word)}")
    
    # Test prefix matching
    print("\nTesting prefix matching:")
    prefixes = ["app", "ban", "ora"]
    for prefix in prefixes:
        print(f"Words with prefix '{prefix}': {trie.get_words_with_prefix(prefix)}")
    
    # Test word count
    print("\nTesting word count:")
    for prefix in prefixes:
        print(f"Count of words with prefix '{prefix}': {trie.get_word_count(prefix)}")
    
    # Test deletion
    print("\nTesting deletion:")
    word_to_delete = "app"
    print(f"Deleting '{word_to_delete}': {trie.delete(word_to_delete)}")
    print(f"Search '{word_to_delete}' after deletion: {trie.search(word_to_delete)}")
    print(f"Words with prefix 'app' after deletion: {trie.get_words_with_prefix('app')}") 