from typing import Any, List, Set as PySet

class Set:
    """Set implementation using a list for simplicity"""
    
    def __init__(self):
        self.items: List[Any] = []
    
    def add(self, item: Any) -> bool:
        """
        Add an item to the set if it doesn't exist
        
        Args:
            item: Item to add
            
        Returns:
            True if item was added, False if it already existed
        """
        if item not in self.items:
            self.items.append(item)
            return True
        return False
    
    def remove(self, item: Any) -> bool:
        """
        Remove an item from the set
        
        Args:
            item: Item to remove
            
        Returns:
            True if item was removed, False if it didn't exist
        """
        if item in self.items:
            self.items.remove(item)
            return True
        return False
    
    def contains(self, item: Any) -> bool:
        """
        Check if an item exists in the set
        
        Args:
            item: Item to check
            
        Returns:
            True if item exists, False otherwise
        """
        return item in self.items
    
    def union(self, other: 'Set') -> 'Set':
        """
        Create a new set containing all items from both sets
        
        Args:
            other: Another set to union with
            
        Returns:
            New set containing all items
        """
        result = Set()
        result.items = list(set(self.items) | set(other.items))
        return result
    
    def intersection(self, other: 'Set') -> 'Set':
        """
        Create a new set containing only items that exist in both sets
        
        Args:
            other: Another set to intersect with
            
        Returns:
            New set containing common items
        """
        result = Set()
        result.items = list(set(self.items) & set(other.items))
        return result
    
    def difference(self, other: 'Set') -> 'Set':
        """
        Create a new set containing items that exist in this set but not in the other
        
        Args:
            other: Another set to compare with
            
        Returns:
            New set containing items unique to this set
        """
        result = Set()
        result.items = list(set(self.items) - set(other.items))
        return result
    
    def size(self) -> int:
        """
        Get number of items in the set
        
        Returns:
            Number of items
        """
        return len(self.items)
    
    def is_empty(self) -> bool:
        """
        Check if set is empty
        
        Returns:
            True if set is empty, False otherwise
        """
        return len(self.items) == 0

# Example usage
if __name__ == "__main__":
    # Create sets
    set1 = Set()
    set2 = Set()
    
    # Test add
    print("Testing add:")
    set1.add(1)
    set1.add(2)
    set1.add(3)
    set2.add(2)
    set2.add(3)
    set2.add(4)
    print(f"Set 1 size: {set1.size()}")
    print(f"Set 2 size: {set2.size()}")
    
    # Test contains
    print("\nTesting contains:")
    print(f"Set 1 contains 2: {set1.contains(2)}")
    print(f"Set 1 contains 4: {set1.contains(4)}")
    
    # Test set operations
    print("\nTesting set operations:")
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)
    
    print(f"Union: {union_set.items}")
    print(f"Intersection: {intersection_set.items}")
    print(f"Difference: {difference_set.items}")
    
    # Test remove
    print("\nTesting remove:")
    print(f"Removed 2 from Set 1: {set1.remove(2)}")
    print(f"Set 1 size after removal: {set1.size()}")
    print(f"Set 1 contains 2: {set1.contains(2)}") 