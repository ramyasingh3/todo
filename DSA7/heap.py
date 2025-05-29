from typing import List, Optional
import heapq

class MinHeap:
    def __init__(self):
        self.heap = []
        
    def push(self, val: int):
        """Add a value to the heap"""
        heapq.heappush(self.heap, val)
        
    def pop(self) -> Optional[int]:
        """Remove and return the minimum value from the heap"""
        return heapq.heappop(self.heap) if self.heap else None
        
    def peek(self) -> Optional[int]:
        """Return the minimum value without removing it"""
        return self.heap[0] if self.heap else None
        
    def size(self) -> int:
        """Return the number of elements in the heap"""
        return len(self.heap)
        
    def is_empty(self) -> bool:
        """Check if the heap is empty"""
        return len(self.heap) == 0
        
    def heapify(self, arr: List[int]):
        """Convert a list into a heap in-place"""
        self.heap = arr
        heapq.heapify(self.heap)
        
    def replace(self, val: int) -> Optional[int]:
        """Replace the minimum value with a new value"""
        if not self.heap:
            return None
        return heapq.heapreplace(self.heap, val)
        
    def merge(self, other_heap: 'MinHeap'):
        """Merge another heap into this heap"""
        self.heap = list(heapq.merge(self.heap, other_heap.heap))
        heapq.heapify(self.heap)

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic operations
    heap1 = MinHeap()
    print("Test Case 1: Basic Operations")
    heap1.push(5)
    heap1.push(3)
    heap1.push(7)
    heap1.push(1)
    heap1.push(9)
    
    print("Heap contents:", heap1.heap)
    print("Minimum value:", heap1.peek())
    print("Popped values:", end=" ")
    while not heap1.is_empty():
        print(heap1.pop(), end=" ")
    print("\n" + "-" * 50)
    
    # Test case 2: Heapify
    print("\nTest Case 2: Heapify")
    arr = [9, 5, 7, 3, 1, 8, 6, 2, 4]
    heap2 = MinHeap()
    heap2.heapify(arr)
    print("Original array:", arr)
    print("Heapified array:", heap2.heap)
    print("-" * 50)
    
    # Test case 3: Replace operation
    print("\nTest Case 3: Replace Operation")
    heap3 = MinHeap()
    heap3.push(5)
    heap3.push(3)
    heap3.push(7)
    print("Before replace:", heap3.heap)
    old_val = heap3.replace(2)
    print(f"Replaced {old_val} with 2")
    print("After replace:", heap3.heap)
    print("-" * 50)
    
    # Test case 4: Merge operation
    print("\nTest Case 4: Merge Operation")
    heap4 = MinHeap()
    heap4.push(1)
    heap4.push(3)
    heap4.push(5)
    
    heap5 = MinHeap()
    heap5.push(2)
    heap5.push(4)
    heap5.push(6)
    
    print("Heap 1:", heap4.heap)
    print("Heap 2:", heap5.heap)
    heap4.merge(heap5)
    print("Merged heap:", heap4.heap)
    print("-" * 50) 