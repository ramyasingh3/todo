from typing import List

def single_number(nums: List[int]) -> int:
    """
    Find the single number in array where every other number appears twice.
    
    Args:
        nums: Array of integers where every number appears twice except one
        
    Returns:
        The single number
        
    Example:
        >>> single_number([4, 1, 2, 1, 2])
        4
    """
    # Using XOR operation
    # a ^ a = 0
    # a ^ 0 = a
    # XOR is associative and commutative
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_hash(nums: List[int]) -> int:
    """
    Find the single number using hash set.
    
    Args:
        nums: Array of integers where every number appears twice except one
        
    Returns:
        The single number
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            seen.remove(num)
        else:
            seen.add(num)
    
    return seen.pop()

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    nums1 = [4, 1, 2, 1, 2]
    print("Test case 1:")
    print(f"Input: nums = {nums1}")
    print(f"Using XOR: {single_number(nums1)}")
    print(f"Using hash set: {single_number_hash(nums1)}")
    
    # Test case 2: Single element
    nums2 = [1]
    print("\nTest case 2:")
    print(f"Input: nums = {nums2}")
    print(f"Using XOR: {single_number(nums2)}")
    print(f"Using hash set: {single_number_hash(nums2)}")
    
    # Test case 3: Negative numbers
    nums3 = [-1, -1, -2]
    print("\nTest case 3:")
    print(f"Input: nums = {nums3}")
    print(f"Using XOR: {single_number(nums3)}")
    print(f"Using hash set: {single_number_hash(nums3)}")
    
    # Test case 4: Larger array
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5, 6, 7, 8]
    print("\nTest case 4:")
    print(f"Input: nums = {nums4}")
    print(f"Using XOR: {single_number(nums4)}")
    print(f"Using hash set: {single_number_hash(nums4)}")
    
    # Test case 5: Zero in array
    nums5 = [0, 1, 0]
    print("\nTest case 5:")
    print(f"Input: nums = {nums5}")
    print(f"Using XOR: {single_number(nums5)}")
    print(f"Using hash set: {single_number_hash(nums5)}") 