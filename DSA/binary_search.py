"""
Binary Search Implementation

This file contains an implementation of the binary search algorithm with detailed explanations
and test cases. Binary search is an efficient algorithm for finding an element in a sorted array.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def binary_search(arr: list, target: int) -> int:
    """
    Perform binary search on a sorted array to find the target value.
    
    Args:
        arr (list): Sorted array of integers
        target (int): Value to search for
        
    Returns:
        int: Index of the target value if found, -1 if not found
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

def test_binary_search():
    """Test cases for binary search implementation"""
    # Test case 1: Target exists in array
    arr1 = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr1, 7) == 3, "Test case 1 failed"
    
    # Test case 2: Target doesn't exist in array
    assert binary_search(arr1, 6) == -1, "Test case 2 failed"
    
    # Test case 3: Target is first element
    assert binary_search(arr1, 1) == 0, "Test case 3 failed"
    
    # Test case 4: Target is last element
    assert binary_search(arr1, 15) == 7, "Test case 4 failed"
    
    # Test case 5: Empty array
    assert binary_search([], 5) == -1, "Test case 5 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    # Run test cases
    test_binary_search()
    
    # Example usage
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    result = binary_search(arr, target)
    
    if result != -1:
        print(f"Element {target} is present at index {result}")
    else:
        print(f"Element {target} is not present in the array")

    # Example usage
    test_cases = [
        ([1, 2, 3, 4, 5], 3),           # Output: 2
        ([1, 2, 3, 4, 5], 6),           # Output: -1
        ([1, 3, 5, 7, 9], 5),           # Output: 2
        ([1, 3, 5, 7, 9], 4),           # Output: -1
        ([1], 1),                       # Output: 0
        ([1], 2),                       # Output: -1
        ([1, 2, 3, 4, 5, 6], 4),        # Output: 3
        ([1, 2, 3, 4, 5, 6], 1),        # Output: 0
        ([1, 2, 3, 4, 5, 6], 6),        # Output: 5
        ([1, 2, 3, 4, 5, 6], 7),        # Output: -1
    ]
    
    for nums, target in test_cases:
        result = binary_search(nums, target)
        print(f"Array: {nums}")
        print(f"Target: {target}")
        print(f"Index: {result}\n")

    # Test cases
    test_arrays = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [1, 3, 5, 7, 9, 11],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [1, 1, 1, 1, 1]
    ]
    
    test_targets = [3, 7, 9, 8, 1]
    
    for arr, target in zip(test_arrays, test_targets):
        result = binary_search(arr, target)
        print(f"Array: {arr}")
        print(f"Target: {target}")
        print(f"Index: {result}")
        print("-" * 30) 