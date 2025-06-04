def max_subarray(nums):
    """
    Find the maximum sum of any contiguous subarray in the given array.
    
    Args:
        nums (List[int]): Input array of integers
        
    Returns:
        int: Maximum sum of any contiguous subarray
    """
    if not nums:
        return 0
        
    current_sum = max_sum = nums[0]
    
    for num in nums[1:]:
        # Choose between starting a new subarray or continuing the current one
        current_sum = max(num, current_sum + num)
        # Update the maximum sum if we found a better subarray
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test cases
def test_max_subarray():
    # Example 1
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert max_subarray(nums1) == 6
    
    # Example 2
    nums2 = [1]
    assert max_subarray(nums2) == 1
    
    # Example 3
    nums3 = [5, 4, -1, 7, 8]
    assert max_subarray(nums3) == 23
    
    # Additional test cases
    nums4 = [-1, -2, -3, -4]
    assert max_subarray(nums4) == -1
    
    nums5 = [1, 2, 3, 4, 5]
    assert max_subarray(nums5) == 15
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_max_subarray() 