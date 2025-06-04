"""
Problem: Find the Second Largest Element in an Array

Given an array of integers, write a function to find the second largest element in the array.
If no second largest exists (due to duplicates), return -1.

Example:
Input: [12, 35, 1, 10, 34, 1]
Output: 34  # Since 35 is largest, 34 is second largest

Input: [10, 10, 10]
Output: -1  # No second largest exists
"""

def find_second_largest(arr):
    if len(arr) < 2:
        return -1
    
    # Initialize largest and second largest
    largest = float('-inf')
    second_largest = float('-inf')
    
    # Find largest and second largest in single pass
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num < largest and num > second_largest:
            second_largest = num
    
    # Check if second largest exists
    if second_largest == float('-inf'):
        return -1
    return second_largest

# Test cases
def test_second_largest():
    test_cases = [
        ([12, 35, 1, 10, 34, 1], 34),
        ([10, 10, 10], -1),
        ([5], -1),
        ([1, 2, 3, 4, 5], 4),
        ([], -1)
    ]
    
    for arr, expected in test_cases:
        result = find_second_largest(arr)
        print(f"Array: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print("Test Passed" if result == expected else "Test Failed")
        print("-" * 30)

if __name__ == "__main__":
    test_second_largest()
