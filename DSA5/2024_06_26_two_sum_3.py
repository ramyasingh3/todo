def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

# Test
if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
