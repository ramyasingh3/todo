from typing import List, Dict, Optional

class TrieNode:
    def __init__(self):
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False
        self.word_count: int = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str):
        """Insert a word into the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word_count += 1
        
    def search(self, word: str) -> bool:
        """Search for a word in the trie"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word
        
    def starts_with(self, prefix: str) -> bool:
        """Check if any word in the trie starts with the given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
        
    def get_words_with_prefix(self, prefix: str) -> List[str]:
        """Get all words that start with the given prefix"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
            
        words = []
        self._collect_words(node, prefix, words)
        return words
        
    def _collect_words(self, node: TrieNode, prefix: str, words: List[str]):
        """Helper method to collect words from a node"""
        if node.is_end_of_word:
            words.append(prefix)
            
        for char, child in node.children.items():
            self._collect_words(child, prefix + char, words)
            
    def delete(self, word: str) -> bool:
        """Delete a word from the trie"""
        def _delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                node.word_count -= 1
                return len(node.children) == 0
                
            char = word[index]
            if char not in node.children:
                return False
                
            should_delete_child = _delete_helper(node.children[char], word, index + 1)
            
            if should_delete_child:
                del node.children[char]
                return len(node.children) == 0
            return False
            
        return _delete_helper(self.root, word, 0)

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic operations
    print("Test Case 1: Basic Operations")
    trie1 = Trie()
    words = ["apple", "app", "application", "banana", "band", "bandana"]
    
    for word in words:
        trie1.insert(word)
        
    print("Words in trie:", words)
    print("Search 'app':", trie1.search("app"))
    print("Search 'orange':", trie1.search("orange"))
    print("Starts with 'ban':", trie1.starts_with("ban"))
    print("Words with prefix 'app':", trie1.get_words_with_prefix("app"))
    print("-" * 50)
    
    # Test case 2: Delete operation
    print("\nTest Case 2: Delete Operation")
    trie2 = Trie()
    trie2.insert("hello")
    trie2.insert("help")
    trie2.insert("hell")
    
    print("Before deletion - Search 'hello':", trie2.search("hello"))
    trie2.delete("hello")
    print("After deletion - Search 'hello':", trie2.search("hello"))
    print("After deletion - Search 'help':", trie2.search("help"))
    print("-" * 50)
    
    # Test case 3: Multiple occurrences
    print("\nTest Case 3: Multiple Occurrences")
    trie3 = Trie()
    trie3.insert("test")
    trie3.insert("test")
    trie3.insert("test")
    
    print("Search 'test':", trie3.search("test"))
    trie3.delete("test")
    print("After one deletion - Search 'test':", trie3.search("test"))
    print("-" * 50) 