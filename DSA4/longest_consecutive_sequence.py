def longestConsecutive(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive elements sequence.
    
    Args:
        nums: List of integers
        
    Returns:
        Length of the longest consecutive sequence
    """
    if not nums:
        return 0
        
    # Convert list to set for O(1) lookups
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start checking from the smallest number in a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                
            max_length = max(max_length, current_length)
            
    return max_length

# Example usage
if __name__ == "__main__":
    # Test case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print(f"Input: {nums1}")
    print(f"Output: {longestConsecutive(nums1)}")  # Expected: 4 (sequence: 1,2,3,4)
    
    # Test case 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print(f"\nInput: {nums2}")
    print(f"Output: {longestConsecutive(nums2)}")  # Expected: 9 (sequence: 0,1,2,3,4,5,6,7,8)
    
    # Test case 3
    nums3 = []
    print(f"\nInput: {nums3}")
    print(f"Output: {longestConsecutive(nums3)}")  # Expected: 0
    
    # Test case 4
    nums4 = [1, 2, 0, 1]
    print(f"\nInput: {nums4}")
    print(f"Output: {longestConsecutive(nums4)}")  # Expected: 3 (sequence: 0,1,2)
    
    # Test case 5
    nums5 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
    print(f"\nInput: {nums5}")
    print(f"Output: {longestConsecutive(nums5)}")  # Expected: 7 (sequence: -1,0,1,3,4,5,6) 