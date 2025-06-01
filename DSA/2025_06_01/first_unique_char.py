from collections import Counter

def first_uniq_char(s: str) -> int:
    """
    Find the first non-repeating character in a string and return its index.
    
    Args:
        s: Input string
        
    Returns:
        Index of first non-repeating character, -1 if none exists
        
    Example:
        >>> first_uniq_char("leetcode")
        0
    """
    # Count frequency of each character
    count = Counter(s)
    
    # Find first character with frequency 1
    for i, char in enumerate(s):
        if count[char] == 1:
            return i
    
    return -1

def first_uniq_char_optimized(s: str) -> int:
    """
    Find the first non-repeating character using a single pass.
    
    Args:
        s: Input string
        
    Returns:
        Index of first non-repeating character, -1 if none exists
    """
    # Store first occurrence of each character
    first_occurrence = {}
    # Store frequency of each character
    frequency = {}
    
    for i, char in enumerate(s):
        if char not in first_occurrence:
            first_occurrence[char] = i
        frequency[char] = frequency.get(char, 0) + 1
    
    # Find minimum index among characters with frequency 1
    min_index = float('inf')
    for char, freq in frequency.items():
        if freq == 1:
            min_index = min(min_index, first_occurrence[char])
    
    return min_index if min_index != float('inf') else -1

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    s1 = "leetcode"
    print("Test case 1:")
    print(f"Input: s = {s1}")
    print(f"Using Counter: {first_uniq_char(s1)}")
    print(f"Using optimized: {first_uniq_char_optimized(s1)}")
    
    # Test case 2: No unique character
    s2 = "aabb"
    print("\nTest case 2:")
    print(f"Input: s = {s2}")
    print(f"Using Counter: {first_uniq_char(s2)}")
    print(f"Using optimized: {first_uniq_char_optimized(s2)}")
    
    # Test case 3: Single character
    s3 = "a"
    print("\nTest case 3:")
    print(f"Input: s = {s3}")
    print(f"Using Counter: {first_uniq_char(s3)}")
    print(f"Using optimized: {first_uniq_char_optimized(s3)}")
    
    # Test case 4: Empty string
    s4 = ""
    print("\nTest case 4:")
    print(f"Input: s = {s4}")
    print(f"Using Counter: {first_uniq_char(s4)}")
    print(f"Using optimized: {first_uniq_char_optimized(s4)}")
    
    # Test case 5: All unique characters
    s5 = "abcde"
    print("\nTest case 5:")
    print(f"Input: s = {s5}")
    print(f"Using Counter: {first_uniq_char(s5)}")
    print(f"Using optimized: {first_uniq_char_optimized(s5)}") 