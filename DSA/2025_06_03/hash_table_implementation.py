from typing import Any, Optional, List, Tuple
from dataclasses import dataclass

@dataclass
class HashEntry:
    """Entry class for Hash Table"""
    key: Any
    value: Any
    next: Optional['HashEntry'] = None

class HashTable:
    """Hash Table implementation using chaining"""
    
    def __init__(self, initial_size: int = 10):
        """
        Initialize hash table
        
        Args:
            initial_size: Initial size of hash table
        """
        self.size = initial_size
        self.table: List[Optional[HashEntry]] = [None] * self.size
        self.count = 0
        self.load_factor = 0.75
    
    def _hash(self, key: Any) -> int:
        """
        Hash function
        
        Args:
            key: Key to hash
            
        Returns:
            Hash value
        """
        return hash(key) % self.size
    
    def _resize(self) -> None:
        """Resize hash table when load factor is exceeded"""
        old_table = self.table
        self.size *= 2
        self.table = [None] * self.size
        self.count = 0
        
        for entry in old_table:
            while entry:
                self.put(entry.key, entry.value)
                entry = entry.next
    
    def put(self, key: Any, value: Any) -> None:
        """
        Insert key-value pair into hash table
        
        Args:
            key: Key to insert
            value: Value to insert
        """
        if self.count / self.size >= self.load_factor:
            self._resize()
        
        index = self._hash(key)
        entry = self.table[index]
        
        # Check if key already exists
        while entry:
            if entry.key == key:
                entry.value = value
                return
            entry = entry.next
        
        # Insert new entry at beginning of chain
        new_entry = HashEntry(key, value, self.table[index])
        self.table[index] = new_entry
        self.count += 1
    
    def get(self, key: Any) -> Optional[Any]:
        """
        Get value for key
        
        Args:
            key: Key to look up
            
        Returns:
            Value for key, or None if not found
        """
        index = self._hash(key)
        entry = self.table[index]
        
        while entry:
            if entry.key == key:
                return entry.value
            entry = entry.next
        
        return None
    
    def remove(self, key: Any) -> bool:
        """
        Remove key-value pair from hash table
        
        Args:
            key: Key to remove
            
        Returns:
            True if key was found and removed, False otherwise
        """
        index = self._hash(key)
        entry = self.table[index]
        prev = None
        
        while entry:
            if entry.key == key:
                if prev:
                    prev.next = entry.next
                else:
                    self.table[index] = entry.next
                self.count -= 1
                return True
            prev = entry
            entry = entry.next
        
        return False
    
    def contains(self, key: Any) -> bool:
        """
        Check if key exists in hash table
        
        Args:
            key: Key to check
            
        Returns:
            True if key exists, False otherwise
        """
        return self.get(key) is not None
    
    def get_size(self) -> int:
        """Get number of key-value pairs in hash table"""
        return self.count

# Example usage
if __name__ == "__main__":
    # Create a hash table
    ht = HashTable()
    
    # Test put and get
    print("Testing put and get:")
    test_data = [
        ("apple", 1),
        ("banana", 2),
        ("cherry", 3),
        ("date", 4),
        ("elderberry", 5)
    ]
    
    for key, value in test_data:
        ht.put(key, value)
        print(f"Put: ({key}, {value})")
        retrieved = ht.get(key)
        print(f"Get {key}: {retrieved}")
    
    # Test contains
    print("\nTesting contains:")
    test_keys = ["apple", "grape", "cherry"]
    for key in test_keys:
        exists = ht.contains(key)
        print(f"Contains {key}: {exists}")
    
    # Test remove
    print("\nTesting remove:")
    for key in ["banana", "date"]:
        removed = ht.remove(key)
        print(f"Remove {key}: {'Success' if removed else 'Failed'}")
        exists = ht.contains(key)
        print(f"Contains {key}: {exists}")
    
    # Test size
    print(f"\nFinal size: {ht.get_size()}") 