from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams of each other.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if strings are anagrams, False otherwise
        
    Example:
        >>> is_anagram("anagram", "nagaram")
        True
    """
    return Counter(s) == Counter(t)

def is_anagram_sorted(s: str, t: str) -> bool:
    """
    Check if two strings are anagrams using sorting.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        True if strings are anagrams, False otherwise
    """
    return sorted(s) == sorted(t)

# Example usage
if __name__ == "__main__":
    # Test case 1: Basic case
    s1, t1 = "anagram", "nagaram"
    print("Test case 1:")
    print(f"Input: s = {s1}, t = {t1}")
    print(f"Using Counter: {is_anagram(s1, t1)}")
    print(f"Using sorting: {is_anagram_sorted(s1, t1)}")
    
    # Test case 2: Different lengths
    s2, t2 = "rat", "car"
    print("\nTest case 2:")
    print(f"Input: s = {s2}, t = {t2}")
    print(f"Using Counter: {is_anagram(s2, t2)}")
    print(f"Using sorting: {is_anagram_sorted(s2, t2)}")
    
    # Test case 3: Empty strings
    s3, t3 = "", ""
    print("\nTest case 3:")
    print(f"Input: s = {s3}, t = {t3}")
    print(f"Using Counter: {is_anagram(s3, t3)}")
    print(f"Using sorting: {is_anagram_sorted(s3, t3)}")
    
    # Test case 4: Same string
    s4, t4 = "hello", "hello"
    print("\nTest case 4:")
    print(f"Input: s = {s4}, t = {t4}")
    print(f"Using Counter: {is_anagram(s4, t4)}")
    print(f"Using sorting: {is_anagram_sorted(s4, t4)}")
    
    # Test case 5: Different characters
    s5, t5 = "abc", "def"
    print("\nTest case 5:")
    print(f"Input: s = {s5}, t = {t5}")
    print(f"Using Counter: {is_anagram(s5, t5)}")
    print(f"Using sorting: {is_anagram_sorted(s5, t5)}") 