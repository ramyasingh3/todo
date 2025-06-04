from typing import Any, Optional
from collections import deque as PyDeque

class Deque:
    """Double-ended queue implementation using collections.deque"""
    
    def __init__(self):
        self.items: PyDeque[Any] = PyDeque()
    
    def add_front(self, item: Any) -> None:
        """
        Add an item to the front of the deque
        
        Args:
            item: Item to be added
        """
        self.items.appendleft(item)
    
    def add_rear(self, item: Any) -> None:
        """
        Add an item to the rear of the deque
        
        Args:
            item: Item to be added
        """
        self.items.append(item)
    
    def remove_front(self) -> Optional[Any]:
        """
        Remove and return the front item
        
        Returns:
            Front item, None if deque is empty
        """
        return self.items.popleft() if not self.is_empty() else None
    
    def remove_rear(self) -> Optional[Any]:
        """
        Remove and return the rear item
        
        Returns:
            Rear item, None if deque is empty
        """
        return self.items.pop() if not self.is_empty() else None
    
    def peek_front(self) -> Optional[Any]:
        """
        Get the front item without removing it
        
        Returns:
            Front item, None if deque is empty
        """
        return self.items[0] if not self.is_empty() else None
    
    def peek_rear(self) -> Optional[Any]:
        """
        Get the rear item without removing it
        
        Returns:
            Rear item, None if deque is empty
        """
        return self.items[-1] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        """
        Check if deque is empty
        
        Returns:
            True if deque is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get number of items in the deque
        
        Returns:
            Number of items
        """
        return len(self.items)

# Example usage
if __name__ == "__main__":
    # Create a deque
    dq = Deque()
    
    # Test adding items
    print("Testing add operations:")
    dq.add_front(1)
    dq.add_rear(2)
    dq.add_front(0)
    dq.add_rear(3)
    print(f"Deque size: {dq.size()}")
    print(f"Front item: {dq.peek_front()}")
    print(f"Rear item: {dq.peek_rear()}")
    
    # Test removing items
    print("\nTesting remove operations:")
    print(f"Removed from front: {dq.remove_front()}")
    print(f"Removed from rear: {dq.remove_rear()}")
    print(f"Deque size: {dq.size()}")
    print(f"Front item: {dq.peek_front()}")
    print(f"Rear item: {dq.peek_rear()}")
    
    # Test empty deque
    print("\nTesting empty deque:")
    print(f"Removed from front: {dq.remove_front()}")
    print(f"Removed from rear: {dq.remove_rear()}")
    print(f"Removed from front: {dq.remove_front()}")  # Should return None
    print(f"Deque is empty: {dq.is_empty()}")
    print(f"Front item: {dq.peek_front()}")  # Should return None
    print(f"Rear item: {dq.peek_rear()}")  # Should return None 