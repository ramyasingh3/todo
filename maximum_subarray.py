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
        
    # Initialize variables
    max_so_far = nums[0]  # Maximum sum found so far
    current_max = nums[0]  # Maximum sum ending at current position
    
    # Iterate through array starting from second element
    for num in nums[1:]:
        # Either extend previous subarray or start new one
        current_max = max(num, current_max + num)
        # Update global maximum
        max_so_far = max(max_so_far, current_max)
    
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
    print(f"Output: {max_subarray(nums3)}")  # Expected: 23 (entire array)
    
    # Test case 4
    nums4 = [-1, -2, -3]
    print(f"\nInput: nums = {nums4}")
    print(f"Output: {max_subarray(nums4)}")  # Expected: -1 (single element) 