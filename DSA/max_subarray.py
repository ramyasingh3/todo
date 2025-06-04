def max_subarray_sum(nums: list[int]) -> int:
    """
    Find the maximum sum of a contiguous subarray using Kadane's Algorithm.
    
    Args:
        nums (list[int]): Input array of integers
        
    Returns:
        int: Maximum sum of a contiguous subarray
    """
    if not nums:
        return 0
        
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in nums:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Example usage
if __name__ == "__main__":
    test_cases = [
        [-2, 1, -3, 4, -1, 2, 1, -5, 4],  # Output: 6 (subarray [4, -1, 2, 1])
        [1],                              # Output: 1
        [5, 4, -1, 7, 8],                # Output: 23
        [-1, -2, -3, -4],                # Output: -1
        [1, 2, 3, 4, 5],                 # Output: 15
        [-2, -3, 4, -1, -2, 1, 5, -3],   # Output: 7
        [2, 3, -2, 4],                   # Output: 7
        [-1, 4, -2, 3, -5, 2],           # Output: 5
    ]
    
    for test in test_cases:
        result = max_subarray_sum(test)
        print(f"Input array: {test}")
        print(f"Maximum subarray sum: {result}\n") 