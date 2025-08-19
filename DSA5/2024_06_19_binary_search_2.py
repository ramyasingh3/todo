def binary_search(nums, target):
    """
    Binary search in sorted array.
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

# Test
if __name__ == "__main__":
    print(binary_search([-1, 0, 3, 5, 9, 12], 9))  # 4
