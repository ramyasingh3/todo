def contains_duplicate(nums):
    """
    Given an integer array nums, return true if any value appears at least twice in the array, 
    and return false if every element is distinct.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

# Test cases
if __name__ == "__main__":
    # Test 1
    nums1 = [1, 2, 3, 1]
    print(f"Input: {nums1}")
    print(f"Output: {contains_duplicate(nums1)}")  # Expected: True
    
    # Test 2
    nums2 = [1, 2, 3, 4]
    print(f"\nInput: {nums2}")
    print(f"Output: {contains_duplicate(nums2)}")  # Expected: False
    
    # Test 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(f"\nInput: {nums3}")
    print(f"Output: {contains_duplicate(nums3)}")  # Expected: True 