# 08_str_str.py

def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    
    if len(needle) > len(haystack):
        return -1
    
    # Check each possible starting position
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i + len(needle)] == needle:
            return i
    
    return -1

# Example usage
if __name__ == "__main__":
    print(str_str("hello", "ll"))  # Output: 2
    print(str_str("aaaaa", "bba"))  # Output: -1
    print(str_str("", ""))  # Output: 0
    print(str_str("mississippi", "issip"))  # Output: 4
    print(str_str("a", "a"))  # Output: 0
    print(str_str("abc", "c"))  # Output: 2
    print(str_str("leetcode", "leeto"))  # Output: -1
    print(str_str("sadbutsad", "sad"))  # Output: 0 