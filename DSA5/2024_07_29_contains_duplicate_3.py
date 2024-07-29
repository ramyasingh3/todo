def contains_duplicate(nums):
    """
    Check if array contains any duplicate elements.
    """
    return len(nums) != len(set(nums))

# Test
if __name__ == "__main__":
    print(contains_duplicate([1, 2, 3, 1]))  # True
