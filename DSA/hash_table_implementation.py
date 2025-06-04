from typing import Any, List, Tuple, Optional
from dataclasses import dataclass

@dataclass
class HashEntry:
    """Entry class for Hash Table"""
    key: Any
    value: Any

class HashTable:
    """Hash Table implementation using chaining for collision resolution"""
    
    def __init__(self, initial_size: int = 10):
        """
        Initialize Hash Table
        
        Args:
            initial_size: Initial size of the hash table
        """
        self.size = initial_size
        self.table: List[List[HashEntry]] = [[] for _ in range(initial_size)]
        self.count = 0
        self.load_factor_threshold = 0.75
    
    def _hash(self, key: Any) -> int:
        """
        Generate hash value for a key
        
        Args:
            key: Key to hash
            
        Returns:
            Hash value
        """
        # Convert key to string and use built-in hash function
        key_str = str(key)
        return hash(key_str) % self.size
    
    def _resize(self) -> None:
        """Resize the hash table when load factor exceeds threshold"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        # Rehash all entries
        for bucket in old_table:
            for entry in bucket:
                self.put(entry.key, entry.value)
    
    def put(self, key: Any, value: Any) -> None:
        """
        Insert or update a key-value pair
        
        Args:
            key: Key to insert/update
            value: Value to associate with key
        """
        # Check if resize is needed
        if (self.count + 1) / self.size > self.load_factor_threshold:
            self._resize()
        
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        # Check if key already exists
        for entry in bucket:
            if entry.key == key:
                entry.value = value
                return
        
        # Add new entry
        bucket.append(HashEntry(key, value))
        self.count += 1
    
    def get(self, key: Any) -> Optional[Any]:
        """
        Get value associated with key
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with key, or None if key not found
        """
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        for entry in bucket:
            if entry.key == key:
                return entry.value
        
        return None
    
    def remove(self, key: Any) -> bool:
        """
        Remove key-value pair
        
        Args:
            key: Key to remove
            
        Returns:
            True if key was found and removed, False otherwise
        """
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        for i, entry in enumerate(bucket):
            if entry.key == key:
                bucket.pop(i)
                self.count -= 1
                return True
        
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
    
    def get_all_entries(self) -> List[Tuple[Any, Any]]:
        """
        Get all key-value pairs in the hash table
        
        Returns:
            List of (key, value) tuples
        """
        entries = []
        for bucket in self.table:
            for entry in bucket:
                entries.append((entry.key, entry.value))
        return entries

# Example usage
if __name__ == "__main__":
    # Create a hash table
    ht = HashTable()
    
    # Test put and get
    print("Testing put and get:")
    test_data = [
        ("name", "John"),
        ("age", 30),
        ("city", "New York"),
        ("occupation", "Developer"),
        ("experience", 5)
    ]
    
    for key, value in test_data:
        ht.put(key, value)
        print(f"Put: {key} -> {value}")
        print(f"Get: {key} -> {ht.get(key)}")
    
    # Test contains
    print("\nTesting contains:")
    test_keys = ["name", "salary", "age", "address"]
    for key in test_keys:
        print(f"Contains {key}: {ht.contains(key)}")
    
    # Test remove
    print("\nTesting remove:")
    key_to_remove = "age"
    print(f"Removing {key_to_remove}: {ht.remove(key_to_remove)}")
    print(f"Contains {key_to_remove} after removal: {ht.contains(key_to_remove)}")
    
    # Show all entries
    print("\nAll entries in hash table:")
    for key, value in ht.get_all_entries():
        print(f"{key} -> {value}") 