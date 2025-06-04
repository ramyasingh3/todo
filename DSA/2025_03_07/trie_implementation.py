from typing import Dict, List, Optional
from dataclasses import dataclass, field

@dataclass
class TrieNode:
    """Node class for Trie"""
    children: Dict[str, 'TrieNode'] = field(default_factory=dict)
    is_end_of_word: bool = False
    value: Optional[str] = None

class Trie:
    """Trie implementation for string operations"""
    
    def __init__(self):
        """Initialize empty trie"""
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        """
        Insert word into trie
        
        Args:
            word: Word to insert
        """
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        current.value = word
    
    def search(self, word: str) -> bool:
        """
        Search for word in trie
        
        Args:
            word: Word to search for
            
        Returns:
            True if word exists, False otherwise
        """
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
        return current.is_end_of_word
    
    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word in trie starts with prefix
        
        Args:
            prefix: Prefix to check
            
        Returns:
            True if prefix exists, False otherwise
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]
        return True
    
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """
        Get all words in trie that start with prefix
        
        Args:
            prefix: Prefix to search for
            
        Returns:
            List of words starting with prefix
        """
        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]
        
        result = []
        self._get_words_helper(current, result)
        return result
    
    def _get_words_helper(self, node: TrieNode, result: List[str]) -> None:
        """Helper method to get all words from a node"""
        if node.is_end_of_word and node.value:
            result.append(node.value)
        
        for child in node.children.values():
            self._get_words_helper(child, result)
    
    def delete(self, word: str) -> bool:
        """
        Delete word from trie
        
        Args:
            word: Word to delete
            
        Returns:
            True if word was deleted, False if word not found
        """
        def delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                node.value = None
                return len(node.children) == 0
            
            char = word[index]
            if char not in node.children:
                return False
            
            should_delete_child = delete_helper(node.children[char], word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0 and not node.is_end_of_word
            
            return False
        
        return delete_helper(self.root, word, 0)
    
    def get_all_words(self) -> List[str]:
        """
        Get all words in trie
        
        Returns:
            List of all words
        """
        result = []
        self._get_words_helper(self.root, result)
        return result

# Example usage
if __name__ == "__main__":
    # Create a trie
    trie = Trie()
    
    # Test insert and search
    print("Testing insert and search:")
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    for word in words:
        trie.insert(word)
        print(f"Inserted: {word}")
    
    # Test search
    print("\nTesting search:")
    test_words = ["apple", "app", "ban", "band", "orange"]
    for word in test_words:
        found = trie.search(word)
        print(f"Searching for {word}: {'Found' if found else 'Not found'}")
    
    # Test prefix search
    print("\nTesting prefix search:")
    prefixes = ["app", "ban", "ora"]
    for prefix in prefixes:
        has_prefix = trie.starts_with(prefix)
        print(f"Starts with {prefix}: {has_prefix}")
    
    # Test get words with prefix
    print("\nTesting get words with prefix:")
    for prefix in prefixes:
        words = trie.get_words_with_prefix(prefix)
        print(f"Words starting with {prefix}: {words}")
    
    # Test delete
    print("\nTesting delete:")
    for word in ["app", "bandana"]:
        deleted = trie.delete(word)
        print(f"Deleted {word}: {'Success' if deleted else 'Failed'}")
        found = trie.search(word)
        print(f"Searching for {word}: {'Found' if found else 'Not found'}")
    
    # Test get all words
    print("\nTesting get all words:")
    all_words = trie.get_all_words()
    print(f"All words in trie: {all_words}") 