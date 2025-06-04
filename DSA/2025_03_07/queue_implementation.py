from typing import Any, Optional
from dataclasses import dataclass

@dataclass
class QueueNode:
    """Node class for Queue"""
    value: Any
    next: Optional['QueueNode'] = None

class Queue:
    """Queue implementation using linked list"""
    
    def __init__(self):
        """Initialize empty queue"""
        self.front: Optional[QueueNode] = None
        self.rear: Optional[QueueNode] = None
        self.size = 0
    
    def enqueue(self, value: Any) -> None:
        """
        Add value to end of queue
        
        Args:
            value: Value to add
        """
        new_node = QueueNode(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
    
    def dequeue(self) -> Any:
        """
        Remove and return value from front of queue
        
        Returns:
            Value from front of queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return value
    
    def peek(self) -> Any:
        """
        Get front value without removing it
        
        Returns:
            Value from front of queue
            
        Raises:
            IndexError: If queue is empty
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.front.value
    
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return self.size == 0
    
    def get_size(self) -> int:
        """Get number of elements in queue"""
        return self.size

# Example usage
if __name__ == "__main__":
    # Create a queue
    queue = Queue()
    
    # Test enqueue
    print("Testing enqueue:")
    values = [1, 2, 3, 4, 5]
    for value in values:
        queue.enqueue(value)
        print(f"Enqueued: {value}")
        print(f"Front element: {queue.peek()}")
        print(f"Queue size: {queue.get_size()}")
    
    # Test dequeue
    print("\nTesting dequeue:")
    while not queue.is_empty():
        value = queue.dequeue()
        print(f"Dequeued: {value}")
        if not queue.is_empty():
            print(f"New front element: {queue.peek()}")
        print(f"Queue size: {queue.get_size()}")
    
    # Test empty queue
    print("\nTesting empty queue:")
    try:
        queue.dequeue()
    except IndexError as e:
        print(f"Error: {e}")
    
    try:
        queue.peek()
    except IndexError as e:
        print(f"Error: {e}") 