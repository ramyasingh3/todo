def binary_search(nums, target):
    """
    Given an array of integers nums which is sorted in ascending order, and an integer target,
    write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
    
    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test cases
if __name__ == "__main__":
    # Test 1
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {binary_search(nums1, target1)}")  # Expected: 4
    
    # Test 2
    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {binary_search(nums2, target2)}")  # Expected: -1
    
    # Test 3
    nums3 = [5]
    target3 = 5
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {binary_search(nums3, target3)}")  # Expected: 0 