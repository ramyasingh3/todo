"""
Find the kth largest element in an unsorted array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Time Complexity:
- Heap solution: O(n log k)
- Quickselect solution: O(n) average case, O(n^2) worst case
Space Complexity:
- Heap solution: O(k)
- Quickselect solution: O(1)
"""

import heapq
from typing import List

def find_kth_largest_heap(nums: List[int], k: int) -> int:
    """
    Solution using a min heap.
    We maintain a min heap of size k, which will contain the k largest elements.
    The root of the heap will be the kth largest element.
    """
    min_heap = []
    
    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)
    
    return min_heap[0]

def partition(nums: List[int], left: int, right: int) -> int:
    """
    Helper function for quickselect that partitions the array around a pivot.
    """
    pivot = nums[right]
    i = left
    
    for j in range(left, right):
        if nums[j] >= pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    
    nums[i], nums[right] = nums[right], nums[i]
    return i

def find_kth_largest_quickselect(nums: List[int], k: int) -> int:
    """
    Solution using quickselect algorithm.
    This is similar to quicksort but we only recurse on the part that contains our target.
    """
    def quickselect(left: int, right: int, k_smallest: int) -> int:
        if left == right:
            return nums[left]
        
        pivot_index = partition(nums, left, right)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return quickselect(left, pivot_index - 1, k_smallest)
        else:
            return quickselect(pivot_index + 1, right, k_smallest)
    
    return quickselect(0, len(nums) - 1, k - 1)

# Test cases
def test_kth_largest():
    test_cases = [
        ([3,2,1,5,6,4], 2, 5),
        ([3,2,3,1,2,4,5,5,6], 4, 4),
        ([1], 1, 1),
        ([2,1], 2, 1),
    ]
    
    for nums, k, expected in test_cases:
        # Test heap solution
        result_heap = find_kth_largest_heap(nums.copy(), k)
        assert result_heap == expected, f"Heap solution failed for {nums}, k={k}. Expected {expected}, got {result_heap}"
        
        # Test quickselect solution
        result_quickselect = find_kth_largest_quickselect(nums.copy(), k)
        assert result_quickselect == expected, f"Quickselect solution failed for {nums}, k={k}. Expected {expected}, got {result_quickselect}"
        
        print(f"Test passed for nums={nums}, k={k}")

if __name__ == "__main__":
    test_kth_largest() 