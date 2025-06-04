from typing import Any, Optional
from heapq import heappush, heappop, heapify

class PriorityQueue:
    """Priority Queue implementation using heapq"""
    
    def __init__(self):
        self.items: list[tuple[int, Any]] = []
        self.counter = 0  # To handle equal priorities
    
    def push(self, item: Any, priority: int = 0) -> None:
        """
        Push an item with priority onto the queue
        
        Args:
            item: Item to be pushed
            priority: Priority of the item (lower number = higher priority)
        """
        heappush(self.items, (priority, self.counter, item))
        self.counter += 1
    
    def pop(self) -> Optional[Any]:
        """
        Pop the highest priority item from the queue
        
        Returns:
            The highest priority item, None if queue is empty
        """
        return heappop(self.items)[2] if not self.is_empty() else None
    
    def peek(self) -> Optional[Any]:
        """
        Get the highest priority item without removing it
        
        Returns:
            The highest priority item, None if queue is empty
        """
        return self.items[0][2] if not self.is_empty() else None
    
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
    # Create a priority queue
    pq = PriorityQueue()
    
    # Test push with priorities
    print("Testing push:")
    pq.push("Task 1", 2)  # Lower priority
    pq.push("Task 2", 1)  # Higher priority
    pq.push("Task 3", 3)  # Lowest priority
    print(f"Queue size: {pq.size()}")
    print(f"Highest priority item: {pq.peek()}")
    
    # Test pop
    print("\nTesting pop:")
    print(f"Popped: {pq.pop()}")  # Should be Task 2
    print(f"Popped: {pq.pop()}")  # Should be Task 1
    print(f"Queue size: {pq.size()}")
    print(f"Highest priority item: {pq.peek()}")
    
    # Test empty queue
    print("\nTesting empty queue:")
    print(f"Popped: {pq.pop()}")
    print(f"Popped: {pq.pop()}")  # Should return None
    print(f"Queue is empty: {pq.is_empty()}")
    print(f"Highest priority item: {pq.peek()}")  # Should return None 