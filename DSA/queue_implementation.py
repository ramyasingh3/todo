from typing import Any, Optional
from collections import deque

class Queue:
    """Queue implementation using collections.deque for efficient operations"""
    
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item: Any) -> None:
        """
        Add an item to the end of the queue
        
        Args:
            item: Item to be added to the queue
        """
        self.items.append(item)
    
    def dequeue(self) -> Any:
        """
        Remove and return the item from the front of the queue
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Queue is empty")
    
    def front(self) -> Any:
        """
        Get the front item without removing it
        
        Returns:
            The front item from the queue
            
        Raises:
            IndexError: If the queue is empty
        """
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")
    
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
    queue.enqueue("First")
    queue.enqueue("Second")
    queue.enqueue("Third")
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
    try:
        print(f"Dequeued: {queue.dequeue()}")  # Should raise IndexError
    except IndexError as e:
        print(f"Error: {e}")
    print(f"Queue is empty: {queue.is_empty()}")
    try:
        print(f"Front element: {queue.front()}")  # Should raise IndexError
    except IndexError as e:
        print(f"Error: {e}") 