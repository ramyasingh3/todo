from typing import Any, List, Optional, TypeVar, Generic
from dataclasses import dataclass
from heapq import heappush, heappop, heapify

T = TypeVar('T')

@dataclass
class HeapItem(Generic[T]):
    """Item class for Min Heap"""
    priority: float
    value: T
    
    def __lt__(self, other: 'HeapItem[T]') -> bool:
        """Compare items by priority"""
        return self.priority < other.priority

class MinHeap(Generic[T]):
    """Min Heap implementation using heapq"""
    
    def __init__(self):
        """Initialize empty min heap"""
        self.heap: List[HeapItem[T]] = []
    
    def push(self, value: T, priority: float) -> None:
        """
        Push value with priority onto heap
        
        Args:
            value: Value to push
            priority: Priority of value
        """
        heappush(self.heap, HeapItem(priority, value))
    
    def pop(self) -> T:
        """
        Pop minimum value from heap
        
        Returns:
            Minimum value
            
        Raises:
            IndexError: If heap is empty
        """
        if self.is_empty():
            raise IndexError("Heap is empty")
        return heappop(self.heap).value
    
    def peek(self) -> T:
        """
        Get minimum value without removing it
        
        Returns:
            Minimum value
            
        Raises:
            IndexError: If heap is empty
        """
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0].value
    
    def is_empty(self) -> bool:
        """Check if heap is empty"""
        return len(self.heap) == 0
    
    def get_size(self) -> int:
        """Get number of elements in heap"""
        return len(self.heap)
    
    def update_priority(self, value: T, new_priority: float) -> bool:
        """
        Update priority of value
        
        Args:
            value: Value to update
            new_priority: New priority
            
        Returns:
            True if value was found and updated, False otherwise
        """
        # Find value in heap
        for i, item in enumerate(self.heap):
            if item.value == value:
                # Update priority
                self.heap[i] = HeapItem(new_priority, value)
                # Reheapify
                heapify(self.heap)
                return True
        return False
    
    def contains(self, value: T) -> bool:
        """
        Check if value exists in heap
        
        Args:
            value: Value to check
            
        Returns:
            True if value exists, False otherwise
        """
        return any(item.value == value for item in self.heap)
    
    def get_priority(self, value: T) -> Optional[float]:
        """
        Get priority of value
        
        Args:
            value: Value to get priority for
            
        Returns:
            Priority of value, or None if not found
        """
        for item in self.heap:
            if item.value == value:
                return item.priority
        return None

# Example usage
if __name__ == "__main__":
    # Create a min heap
    heap = MinHeap[str]()
    
    # Test push
    print("Testing push:")
    items = [
        ("Task A", 5),
        ("Task B", 3),
        ("Task C", 7),
        ("Task D", 1),
        ("Task E", 4)
    ]
    
    for value, priority in items:
        heap.push(value, priority)
        print(f"Pushed: {value} (priority: {priority})")
        print(f"Minimum: {heap.peek()}")
        print(f"Heap size: {heap.get_size()}")
    
    # Test pop
    print("\nTesting pop:")
    while not heap.is_empty():
        value = heap.pop()
        print(f"Popped: {value}")
        if not heap.is_empty():
            print(f"New minimum: {heap.peek()}")
        print(f"Heap size: {heap.get_size()}")
    
    # Test empty heap
    print("\nTesting empty heap:")
    try:
        heap.pop()
    except IndexError as e:
        print(f"Error: {e}")
    
    try:
        heap.peek()
    except IndexError as e:
        print(f"Error: {e}")
    
    # Test update priority
    print("\nTesting update priority:")
    heap.push("Task X", 10)
    heap.push("Task Y", 20)
    heap.push("Task Z", 15)
    
    print("Before update:")
    print(f"Minimum: {heap.peek()}")
    
    updated = heap.update_priority("Task Y", 5)
    print(f"Updated Task Y priority: {updated}")
    
    print("After update:")
    print(f"Minimum: {heap.peek()}")
    
    # Test contains and get_priority
    print("\nTesting contains and get_priority:")
    test_values = ["Task X", "Task Y", "Task W"]
    for value in test_values:
        exists = heap.contains(value)
        priority = heap.get_priority(value)
        print(f"Contains {value}: {exists}")
        if priority is not None:
            print(f"Priority of {value}: {priority}") 