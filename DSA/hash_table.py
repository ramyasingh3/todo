from typing import Any, Optional, List, Tuple

class HashTable:
    """Hash Table implementation with chaining for collision resolution"""
    
    def __init__(self, size: int = 10):
        self.size = size
        self.table: List[List[Tuple[str, Any]]] = [[] for _ in range(size)]
        self.count = 0
    
    def _hash(self, key: str) -> int:
        """
        Generate hash value for a key
        
        Args:
            key: Key to hash
            
        Returns:
            Hash value
        """
        return sum(ord(c) for c in key) % self.size
    
    def put(self, key: str, value: Any) -> None:
        """
        Insert or update a key-value pair
        
        Args:
            key: Key to insert/update
            value: Value to associate with key
        """
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        # Check if key exists
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        
        # Key doesn't exist, add new pair
        bucket.append((key, value))
        self.count += 1
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get value for a key
        
        Args:
            key: Key to look up
            
        Returns:
            Value associated with key, None if key not found
        """
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def remove(self, key: str) -> Optional[Any]:
        """
        Remove a key-value pair
        
        Args:
            key: Key to remove
            
        Returns:
            Value that was removed, None if key not found
        """
        hash_value = self._hash(key)
        bucket = self.table[hash_value]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self.count -= 1
                return v
        return None
    
    def size(self) -> int:
        """
        Get number of key-value pairs
        
        Returns:
            Number of pairs in the table
        """
        return self.count
    
    def is_empty(self) -> bool:
        """
        Check if table is empty
        
        Returns:
            True if table is empty, False otherwise
        """
        return self.count == 0

# Example usage
if __name__ == "__main__":
    # Create a hash table
    ht = HashTable()
    
    # Test put and get
    print("Testing put and get:")
    ht.put("apple", 1)
    ht.put("banana", 2)
    ht.put("cherry", 3)
    print(f"Value for 'apple': {ht.get('apple')}")
    print(f"Value for 'banana': {ht.get('banana')}")
    print(f"Value for 'cherry': {ht.get('cherry')}")
    print(f"Value for 'orange': {ht.get('orange')}")  # Should return None
    
    # Test update
    print("\nTesting update:")
    ht.put("apple", 4)
    print(f"Updated value for 'apple': {ht.get('apple')}")
    
    # Test remove
    print("\nTesting remove:")
    print(f"Removed value: {ht.remove('banana')}")
    print(f"Value for 'banana' after removal: {ht.get('banana')}")
    
    # Test size and empty
    print("\nTesting size and empty:")
    print(f"Size: {ht.size()}")
    print(f"Is empty: {ht.is_empty()}") 