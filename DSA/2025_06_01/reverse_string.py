from typing import List

def reverse_string(s: List[str]) -> None:
    """
    Reverse a string in-place.
    
    Args:
        s: List of characters to be reversed
        
    Example:
        >>> s = ["h","e","l","l","o"]
        >>> reverse_string(s)
        >>> s
        ['o', 'l', 'l', 'e', 'h']
    """
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

def reverse_string_recursive(s: List[str]) -> None:
    """
    Reverse a string in-place using recursion.
    
    Args:
        s: List of characters to be reversed
    """
    def reverse(left: int, right: int) -> None:
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        reverse(left + 1, right - 1)
    
    reverse(0, len(s) - 1)

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    s1 = ["h", "e", "l", "l", "o"]
    print("Test case 1:")
    print(f"Input: s = {s1}")
    reverse_string(s1)
    print(f"Using iteration: {s1}")
    
    # Test case 2: Single character
    s2 = ["a"]
    print("\nTest case 2:")
    print(f"Input: s = {s2}")
    reverse_string(s2)
    print(f"Using iteration: {s2}")
    
    # Test case 3: Empty list
    s3 = []
    print("\nTest case 3:")
    print(f"Input: s = {s3}")
    reverse_string(s3)
    print(f"Using iteration: {s3}")
    
    # Test case 4: Even length
    s4 = ["a", "b", "c", "d"]
    print("\nTest case 4:")
    print(f"Input: s = {s4}")
    reverse_string(s4)
    print(f"Using iteration: {s4}")
    
    # Test case 5: Odd length
    s5 = ["a", "b", "c", "d", "e"]
    print("\nTest case 5:")
    print(f"Input: s = {s5}")
    reverse_string(s5)
    print(f"Using iteration: {s5}")
    
    # Test recursive solution
    s6 = ["h", "e", "l", "l", "o"]
    print("\nTest recursive solution:")
    print(f"Input: s = {s6}")
    reverse_string_recursive(s6)
    print(f"Using recursion: {s6}") 