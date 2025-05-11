def maxSubArray(nums: list[int]) -> int:
    """
    Find the contiguous subarray with the largest sum.
    
    Args:
        nums: List of integers
        
    Returns:
        Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
        
    max_so_far = nums[0]
    current_max = nums[0]
    
    for num in nums[1:]:
        # Either extend the previous subarray or start a new one
        current_max = max(num, current_max + num)
        # Update the global maximum
        max_so_far = max(max_so_far, current_max)
    
    return max_so_far

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Input: {nums1}")
    print(f"Output: {maxSubArray(nums1)}")  # Expected: 6 (subarray [4,-1,2,1])
    
    # Test case 2
    nums2 = [1]
    print(f"\nInput: {nums2}")
    print(f"Output: {maxSubArray(nums2)}")  # Expected: 1
    
    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    print(f"\nInput: {nums3}")
    print(f"Output: {maxSubArray(nums3)}")  # Expected: 23
    
    # Test case 4
    nums4 = [-1, -2, -3, -4]
    print(f"\nInput: {nums4}")
    print(f"Output: {maxSubArray(nums4)}")  # Expected: -1 