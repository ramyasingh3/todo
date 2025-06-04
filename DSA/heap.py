from typing import List, Optional
import heapq

class MinHeap:
    """Min Heap implementation using heapq"""
    
    def __init__(self):
        self.heap: List[int] = []
    
    def push(self, val: int) -> None:
        """
        Push a value into the heap
        
        Args:
            val: Value to be pushed
        """
        heapq.heappush(self.heap, val)
    
    def pop(self) -> Optional[int]:
        """
        Pop the minimum value from the heap
        
        Returns:
            Minimum value if heap is not empty, None otherwise
        """
        return heapq.heappop(self.heap) if self.heap else None
    
    def peek(self) -> Optional[int]:
        """
        Get the minimum value without removing it
        
        Returns:
            Minimum value if heap is not empty, None otherwise
        """
        return self.heap[0] if self.heap else None
    
    def size(self) -> int:
        """
        Get the size of the heap
        
        Returns:
            Number of elements in the heap
        """
        return len(self.heap)
    
    def is_empty(self) -> bool:
        """
        Check if the heap is empty
        
        Returns:
            True if heap is empty, False otherwise
        """
        return len(self.heap) == 0

class MaxHeap:
    """Max Heap implementation using heapq with negated values"""
    
    def __init__(self):
        self.heap: List[int] = []
    
    def push(self, val: int) -> None:
        """
        Push a value into the heap
        
        Args:
            val: Value to be pushed
        """
        heapq.heappush(self.heap, -val)  # Negate the value for max heap
    
    def pop(self) -> Optional[int]:
        """
        Pop the maximum value from the heap
        
        Returns:
            Maximum value if heap is not empty, None otherwise
        """
        return -heapq.heappop(self.heap) if self.heap else None
    
    def peek(self) -> Optional[int]:
        """
        Get the maximum value without removing it
        
        Returns:
            Maximum value if heap is not empty, None otherwise
        """
        return -self.heap[0] if self.heap else None
    
    def size(self) -> int:
        """
        Get the size of the heap
        
        Returns:
            Number of elements in the heap
        """
        return len(self.heap)
    
    def is_empty(self) -> bool:
        """
        Check if the heap is empty
        
        Returns:
            True if heap is empty, False otherwise
        """
        return len(self.heap) == 0

# Example usage
if __name__ == "__main__":
    # Test MinHeap
    print("Testing MinHeap:")
    min_heap = MinHeap()
    
    # Push values
    values = [5, 3, 7, 1, 9, 2, 6, 4, 8]
    for val in values:
        min_heap.push(val)
        print(f"Pushed {val}, Min value: {min_heap.peek()}")
    
    # Pop values
    print("\nPopping values from MinHeap:")
    while not min_heap.is_empty():
        val = min_heap.pop()
        print(f"Popped {val}, Size: {min_heap.size()}")
    
    # Test MaxHeap
    print("\nTesting MaxHeap:")
    max_heap = MaxHeap()
    
    # Push values
    for val in values:
        max_heap.push(val)
        print(f"Pushed {val}, Max value: {max_heap.peek()}")
    
    # Pop values
    print("\nPopping values from MaxHeap:")
    while not max_heap.is_empty():
        val = max_heap.pop()
        print(f"Popped {val}, Size: {max_heap.size()}")
    
    # Test edge cases
    print("\nTesting edge cases:")
    empty_heap = MinHeap()
    print(f"Empty heap peek: {empty_heap.peek()}")
    print(f"Empty heap pop: {empty_heap.pop()}")
    print(f"Is empty: {empty_heap.is_empty()}")
    print(f"Size: {empty_heap.size()}") 