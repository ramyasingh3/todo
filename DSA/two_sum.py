"""
Two Sum Problem Implementation

This file contains multiple implementations of the Two Sum problem:
1. Brute Force Approach (O(n²))
2. Hash Map Approach (O(n))

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Time Complexity:
- Brute Force: O(n²)
- Hash Map: O(n)

Space Complexity:
- Brute Force: O(1)
- Hash Map: O(n)
"""

def two_sum_brute_force(nums, target):
    """
    Brute force approach to find two numbers that sum up to target.
    
    Args:
        nums (list): List of integers
        target (int): Target sum
        
    Returns:
        tuple: Indices of the two numbers that sum up to target
    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None

def two_sum_hash_map(nums, target):
    """
    Hash map approach to find two numbers that sum up to target.
    
    Args:
        nums (list): List of integers
        target (int): Target sum
        
    Returns:
        tuple: Indices of the two numbers that sum up to target
    """
    num_map = {}  # val -> index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return (num_map[complement], i)
        num_map[num] = i
    return None

def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in the array that add up to the target value.
    
    Args:
        nums: List of integers
        target: Target sum to find
        
    Returns:
        list[int]: Indices of the two numbers that add up to target
        
    Example:
        >>> two_sum([2, 7, 11, 15], 9)
        [0, 1]
        >>> two_sum([3, 2, 4], 6)
        [1, 2]
    """
    # Dictionary to store number -> index mapping
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed
        complement = target - num
        
        # If complement exists in map, we found our pair
        if complement in num_map:
            return [num_map[complement], i]
            
        # Store current number and its index
        num_map[num] = i
    
    # No solution found
    return []

def test_two_sum():
    """Test cases for both two sum implementations"""
    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert two_sum_brute_force(nums1, target1) == (0, 1), "Brute force test case 1 failed"
    assert two_sum_hash_map(nums1, target1) == (0, 1), "Hash map test case 1 failed"
    
    # Test case 2: Numbers at the end
    nums2 = [3, 2, 4]
    target2 = 6
    assert two_sum_brute_force(nums2, target2) == (1, 2), "Brute force test case 2 failed"
    assert two_sum_hash_map(nums2, target2) == (1, 2), "Hash map test case 2 failed"
    
    # Test case 3: Same number twice
    nums3 = [3, 3]
    target3 = 6
    assert two_sum_brute_force(nums3, target3) == (0, 1), "Brute force test case 3 failed"
    assert two_sum_hash_map(nums3, target3) == (0, 1), "Hash map test case 3 failed"
    
    # Test case 4: No solution
    nums4 = [1, 2, 3, 4]
    target4 = 10
    assert two_sum_brute_force(nums4, target4) is None, "Brute force test case 4 failed"
    assert two_sum_hash_map(nums4, target4) is None, "Hash map test case 4 failed"
    
    print("All test cases passed!")

def test_solution():
    # Test cases
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),      # Basic case
        ([3, 2, 4], 6, [1, 2]),           # Middle elements
        ([3, 3], 6, [0, 1]),              # Same numbers
        ([1, 5, 8, 3], 8, [0, 3]),        # First and last
        ([4, 2, 6, 8], 10, [0, 3]),       # Even numbers
        ([1, 3, 5, 7], 12, [2, 3]),       # Odd numbers
        ([0, 4, 3, 0], 0, [0, 3]),        # Zeroes
        ([-1, -2, -3, -4], -7, [2, 3]),   # Negative numbers
        ([1, 2, 3, 4], 8, []),            # No solution
        ([], 5, []),                       # Empty array
    ]
    
    print("Running test cases for Two Sum problem:")
    print("-" * 50)
    
    for nums, target, expected in test_cases:
        result = two_sum(nums, target)
        print(f"Input: nums = {nums}, target = {target}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'PASSED' if result == expected else 'FAILED'}")
        print("-" * 50)

if __name__ == "__main__":
    # Run test cases
    test_two_sum()
    
    # Example usage
    nums = [2, 7, 11, 15]
    target = 9
    
    # Using brute force approach
    result_brute = two_sum_brute_force(nums, target)
    print(f"Brute Force Result: {result_brute}")
    
    # Using hash map approach
    result_hash = two_sum_hash_map(nums, target)
    print(f"Hash Map Result: {result_hash}")
    
    if result_hash:
        print(f"Numbers at indices {result_hash} sum up to {target}")
        print(f"Numbers are: {nums[result_hash[0]]} and {nums[result_hash[1]]}")

    test_solution() 