from typing import List, Callable
import mmh3  # MurmurHash3 for efficient hashing

class BloomFilter:
    """Bloom Filter implementation using bit array and multiple hash functions"""
    
    def __init__(self, size: int = 1000, num_hashes: int = 3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [False] * size
    
    def _get_hash_values(self, item: str) -> List[int]:
        """
        Get hash values for an item using different seeds
        
        Args:
            item: Item to hash
            
        Returns:
            List of hash values
        """
        return [mmh3.hash(item, seed=i) % self.size for i in range(self.num_hashes)]
    
    def add(self, item: str) -> None:
        """
        Add an item to the bloom filter
        
        Args:
            item: Item to add
        """
        for hash_value in self._get_hash_values(item):
            self.bit_array[hash_value] = True
    
    def contains(self, item: str) -> bool:
        """
        Check if an item might be in the bloom filter
        
        Args:
            item: Item to check
            
        Returns:
            True if item might be present, False if definitely not present
        """
        return all(self.bit_array[hash_value] for hash_value in self._get_hash_values(item))
    
    def clear(self) -> None:
        """Clear all items from the bloom filter"""
        self.bit_array = [False] * self.size

# Example usage
if __name__ == "__main__":
    # Create a bloom filter
    bloom = BloomFilter(size=100, num_hashes=3)
    
    # Test adding items
    print("Testing add operations:")
    bloom.add("apple")
    bloom.add("banana")
    bloom.add("cherry")
    
    # Test checking items
    print("\nTesting contains operations:")
    print(f"Contains 'apple': {bloom.contains('apple')}")  # Should be True
    print(f"Contains 'banana': {bloom.contains('banana')}")  # Should be True
    print(f"Contains 'cherry': {bloom.contains('cherry')}")  # Should be True
    print(f"Contains 'orange': {bloom.contains('orange')}")  # Should be False
    
    # Test false positives
    print("\nTesting false positives:")
    bloom.add("grape")
    print(f"Contains 'grape': {bloom.contains('grape')}")  # Should be True
    print(f"Contains 'grapefruit': {bloom.contains('grapefruit')}")  # Might be True (false positive)
    
    # Test clearing
    print("\nTesting clear operation:")
    bloom.clear()
    print(f"Contains 'apple': {bloom.contains('apple')}")  # Should be False
    print(f"Contains 'banana': {bloom.contains('banana')}")  # Should be False 