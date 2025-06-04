from typing import Any, Optional
from collections import OrderedDict

class LRUCache:
    """Least Recently Used (LRU) cache implementation using OrderedDict"""
    
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.cache: OrderedDict[Any, Any] = OrderedDict()
    
    def get(self, key: Any) -> Optional[Any]:
        """
        Get value for key if it exists, otherwise return None
        
        Args:
            key: Key to look up
            
        Returns:
            Value if key exists, None otherwise
        """
        if key not in self.cache:
            return None
            
        # Move key to end (most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key: Any, value: Any) -> None:
        """
        Add or update value for key
        
        Args:
            key: Key to add/update
            value: Value to store
        """
        if key in self.cache:
            # Remove existing key
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            # Remove least recently used item
            self.cache.popitem(last=False)
            
        # Add new key-value pair
        self.cache[key] = value
    
    def remove(self, key: Any) -> bool:
        """
        Remove key from cache
        
        Args:
            key: Key to remove
            
        Returns:
            True if key was removed, False if key didn't exist
        """
        if key in self.cache:
            self.cache.pop(key)
            return True
        return False
    
    def clear(self) -> None:
        """Clear all items from cache"""
        self.cache.clear()
    
    def get_size(self) -> int:
        """
        Get number of items in cache
        
        Returns:
            Number of items
        """
        return len(self.cache)
    
    def is_full(self) -> bool:
        """
        Check if cache is full
        
        Returns:
            True if cache is full, False otherwise
        """
        return len(self.cache) >= self.capacity

# Example usage
if __name__ == "__main__":
    # Create an LRU cache with capacity 3
    cache = LRUCache(3)
    
    # Test putting items
    print("Testing put operations:")
    cache.put(1, "one")
    cache.put(2, "two")
    cache.put(3, "three")
    print(f"Cache size: {cache.get_size()}")
    
    # Test getting items
    print("\nTesting get operations:")
    print(f"Get 1: {cache.get(1)}")
    print(f"Get 2: {cache.get(2)}")
    print(f"Get 4: {cache.get(4)}")  # Should return None
    
    # Test LRU behavior
    print("\nTesting LRU behavior:")
    cache.put(4, "four")  # Should remove 3 (least recently used)
    print(f"Get 3: {cache.get(3)}")  # Should return None
    print(f"Get 4: {cache.get(4)}")
    
    # Test removing items
    print("\nTesting remove operation:")
    print(f"Remove 2: {cache.remove(2)}")
    print(f"Get 2: {cache.get(2)}")  # Should return None
    
    # Test clearing cache
    print("\nTesting clear operation:")
    cache.clear()
    print(f"Cache size: {cache.get_size()}")
    print(f"Get 1: {cache.get(1)}")  # Should return None 