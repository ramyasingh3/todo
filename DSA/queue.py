from typing import Any, Optional
from collections import deque

class Queue:
    """Queue implementation using deque for efficient operations"""
    
    def __init__(self):
        self.items: deque[Any] = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the end of the queue
        
        Args:
            item: Item to be added
        """
        self.items.append(item)
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the first item from the queue
        
        Returns:
            The first item, None if queue is empty
        """
        return self.items.popleft() if not self.is_empty() else None
    
    def front(self) -> Optional[Any]:
        """
        Get the first item without removing it
        
        Returns:
            The first item, None if queue is empty
        """
        return self.items[0] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        """
        Check if the queue is empty
        
        Returns:
            True if queue is empty, False otherwise
        """
        return len(self.items) == 0
    
    def size(self) -> int:
        """
        Get the number of items in the queue
        
        Returns:
            Number of items in the queue
        """
        return len(self.items)

# Example usage
if __name__ == "__main__":
    # Create a queue
    queue = Queue()
    
    # Test enqueue
    print("Testing enqueue:")
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(f"Queue size: {queue.size()}")
    print(f"Front element: {queue.front()}")
    
    # Test dequeue
    print("\nTesting dequeue:")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Queue size: {queue.size()}")
    print(f"Front element: {queue.front()}")
    
    # Test empty queue
    print("\nTesting empty queue:")
    print(f"Dequeued: {queue.dequeue()}")
    print(f"Dequeued: {queue.dequeue()}")  # Should return None
    print(f"Queue is empty: {queue.is_empty()}")
    print(f"Front element: {queue.front()}")  # Should return None 