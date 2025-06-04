# 04_first_non_repeating.py

def first_non_repeating(s: str) -> str:
    # Count frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first character with count 1
    for char in s:
        if char_count[char] == 1:
            return char
    
    return ""  # Return empty string if no non-repeating character found

# Example usage
if __name__ == "__main__":
    print(first_non_repeating("leetcode"))  # Output: "l"
    print(first_non_repeating("hello"))  # Output: "h"
    print(first_non_repeating("aabbcc"))  # Output: ""
    print(first_non_repeating("python"))  # Output: "p"
    print(first_non_repeating("aabbccd"))  # Output: "d"
    print(first_non_repeating(""))  # Output: ""
    print(first_non_repeating("a"))  # Output: "a"
    print(first_non_repeating("aa"))  # Output: "" 