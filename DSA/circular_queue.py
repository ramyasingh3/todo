from typing import Any, Optional

class CircularQueue:
    """Circular Queue implementation using a fixed-size array"""
    
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.items: list[Optional[Any]] = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def enqueue(self, item: Any) -> bool:
        """
        Add an item to the queue
        
        Args:
            item: Item to be added
            
        Returns:
            True if item was added, False if queue is full
        """
        if self.is_full():
            return False
            
        self.rear = (self.rear + 1) % self.capacity
        self.items[self.rear] = item
        self.size += 1
        return True
    
    def dequeue(self) -> Optional[Any]:
        """
        Remove and return the front item
        
        Returns:
            Front item, None if queue is empty
        """
        if self.is_empty():
            return None
            
        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def peek(self) -> Optional[Any]:
        """
        Get the front item without removing it
        
        Returns:
            Front item, None if queue is empty
        """
        return self.items[self.front] if not self.is_empty() else None
    
    def is_empty(self) -> bool:
        """
        Check if queue is empty
        
        Returns:
            True if queue is empty, False otherwise
        """
        return self.size == 0
    
    def is_full(self) -> bool:
        """
        Check if queue is full
        
        Returns:
            True if queue is full, False otherwise
        """
        return self.size == self.capacity
    
    def get_size(self) -> int:
        """
        Get number of items in the queue
        
        Returns:
            Number of items
        """
        return self.size

# Example usage
if __name__ == "__main__":
    # Create a circular queue
    cq = CircularQueue(3)
    
    # Test enqueue
    print("Testing enqueue:")
    print(f"Enqueued 1: {cq.enqueue(1)}")
    print(f"Enqueued 2: {cq.enqueue(2)}")
    print(f"Enqueued 3: {cq.enqueue(3)}")
    print(f"Enqueued 4: {cq.enqueue(4)}")  # Should fail
    print(f"Queue size: {cq.get_size()}")
    print(f"Front item: {cq.peek()}")
    
    # Test dequeue
    print("\nTesting dequeue:")
    print(f"Dequeued: {cq.dequeue()}")
    print(f"Dequeued: {cq.dequeue()}")
    print(f"Queue size: {cq.get_size()}")
    print(f"Front item: {cq.peek()}")
    
    # Test circular behavior
    print("\nTesting circular behavior:")
    print(f"Enqueued 4: {cq.enqueue(4)}")
    print(f"Enqueued 5: {cq.enqueue(5)}")
    print(f"Queue size: {cq.get_size()}")
    print(f"Front item: {cq.peek()}")
    
    # Test empty queue
    print("\nTesting empty queue:")
    print(f"Dequeued: {cq.dequeue()}")
    print(f"Dequeued: {cq.dequeue()}")
    print(f"Dequeued: {cq.dequeue()}")
    print(f"Dequeued: {cq.dequeue()}")  # Should return None
    print(f"Queue is empty: {cq.is_empty()}")
    print(f"Front item: {cq.peek()}")  # Should return None 