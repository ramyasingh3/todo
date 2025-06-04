def max_subarray(nums: list[int]) -> int:
    """
    Find the sum of the contiguous subarray with the largest sum.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
        
    max_so_far = float('-inf')
    max_ending_here = 0
    
    for num in nums:
        # Either extend the previous subarray or start a new one
        max_ending_here = max(num, max_ending_here + num)
        # Update the global maximum
        max_so_far = max(max_so_far, max_ending_here)
    
    return max_so_far

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: nums = {nums1}")
    print(f"Output: {max_subarray(nums1)}")  # Expected: 6 (subarray [4,-1,2,1])
    
    # Test case 2
    nums2 = [1]
    print(f"\nInput: nums = {nums2}")
    print(f"Output: {max_subarray(nums2)}")  # Expected: 1
    
    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    print(f"\nInput: nums = {nums3}")
    print(f"Output: {max_subarray(nums3)}")  # Expected: 23 (subarray [5,4,-1,7,8]) 