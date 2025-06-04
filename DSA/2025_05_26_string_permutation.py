# 13_string_permutation.py

def is_permutation(s1: str, s2: str) -> bool:
    # If lengths are different, they can't be permutations
    if len(s1) != len(s2):
        return False
    
    # Count characters in first string
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Decrement counts for second string
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True

# Example usage
if __name__ == "__main__":
    print(is_permutation("abc", "cba"))  # Output: True
    print(is_permutation("hello", "world"))  # Output: False
    print(is_permutation("", ""))  # Output: True
    print(is_permutation("a", "a"))  # Output: True
    print(is_permutation("a", "b"))  # Output: False
    print(is_permutation("python", "nohtyp"))  # Output: True
    print(is_permutation("listen", "silent"))  # Output: True
    print(is_permutation("rat", "car"))  # Output: False
    print(is_permutation("anagram", "nagaram"))  # Output: True 