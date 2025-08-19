def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    
    return []

# Test cases
if __name__ == "__main__":
    # Test 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {two_sum(nums1, target1)}")  # Expected: [0, 1]
    
    # Test 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {two_sum(nums2, target2)}")  # Expected: [1, 2]
    
    # Test 3
    nums3 = [3, 3]
    target3 = 6
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {two_sum(nums3, target3)}")  # Expected: [0, 1] 